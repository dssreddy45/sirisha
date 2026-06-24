# ============================================================
# ai_api_service.py — Production AI API Service
# Paste ALL of this into ONE Colab cell and run it
# ============================================================

# STEP 1: Install dependencies
import subprocess
subprocess.run(["pip", "install", "-q", "fastapi", "uvicorn", "nest-asyncio", "httpx"], check=True)

# STEP 2: Imports
import asyncio, logging, math, time, uuid
from datetime import datetime
from typing import List, Optional

import nest_asyncio
import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, validator

nest_asyncio.apply()

# STEP 3: Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("ai_api")

# STEP 4: App
app = FastAPI(
    title="AI API Service",
    description="Production-grade AI API — Chat, Embeddings, Search",
    version="1.0.0",
)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# STEP 5: Models
class ChatMessage(BaseModel):
    role: str = Field(..., description="user | assistant | system")
    content: str = Field(..., min_length=1, max_length=32000)

    @validator("role")
    def valid_role(cls, v):
        if v not in ("user", "assistant", "system"):
            raise ValueError("role must be user, assistant, or system")
        return v

    @validator("content")
    def not_blank(cls, v):
        if not v.strip():
            raise ValueError("content must not be blank")
        return v

class ChatRequest(BaseModel):
    messages: List[ChatMessage] = Field(..., min_items=1)
    model: Optional[str] = "gpt-4o"
    temperature: Optional[float] = Field(0.7, ge=0.0, le=2.0)
    max_tokens: Optional[int] = Field(1024, ge=1, le=8192)

    @validator("messages")
    def needs_user_msg(cls, v):
        if not any(m.role == "user" for m in v):
            raise ValueError("At least one message must have role=user")
        return v

class ChatResponse(BaseModel):
    id: str
    model: str
    created: int
    message: ChatMessage
    usage: dict
    latency_ms: float

class EmbeddingRequest(BaseModel):
    input: List[str] = Field(..., min_items=1, max_items=100)
    model: Optional[str] = "text-embedding-3-small"

    @validator("input", each_item=True)
    def input_valid(cls, v):
        if not v.strip():
            raise ValueError("Each input must not be blank")
        if len(v) > 8192:
            raise ValueError("Input exceeds 8192 character limit")
        return v

class EmbeddingResponse(BaseModel):
    id: str
    model: str
    embeddings: List[List[float]]
    dimensions: int
    token_count: int
    latency_ms: float

class SearchRequest(BaseModel):
    query: str = Field(..., min_length=1, max_length=1000)
    top_k: Optional[int] = Field(5, ge=1, le=20)
    threshold: Optional[float] = Field(0.0, ge=0.0, le=1.0)

    @validator("query")
    def query_not_blank(cls, v):
        if not v.strip():
            raise ValueError("query must not be blank")
        return v

class SearchResult(BaseModel):
    id: str
    content: str
    score: float
    metadata: dict

class SearchResponse(BaseModel):
    id: str
    query: str
    results: List[SearchResult]
    total_found: int
    latency_ms: float

# STEP 6: Mock document store
DOCS = [
    {"id": "doc-001", "content": "FastAPI is a modern, fast web framework for building APIs with Python.", "tags": ["python", "api"]},
    {"id": "doc-002", "content": "Uvicorn is a lightning-fast ASGI server using uvloop and httptools.", "tags": ["server", "asgi"]},
    {"id": "doc-003", "content": "RAG combines vector search with LLM generation for grounded answers.", "tags": ["rag", "llm", "ai"]},
    {"id": "doc-004", "content": "Embeddings are dense vector representations used for semantic search.", "tags": ["embeddings", "nlp"]},
    {"id": "doc-005", "content": "Production AI systems require observability, cost tracking, and security guardrails.", "tags": ["production", "mlops"]},
    {"id": "doc-006", "content": "LangGraph and CrewAI are orchestration frameworks for LLM-powered applications.", "tags": ["orchestration", "llm"]},
    {"id": "doc-007", "content": "Vector databases like Pinecone, Qdrant, and pgvector store high-dimensional embeddings.", "tags": ["vector-db", "search"]},
    {"id": "doc-008", "content": "Semantic caching reduces LLM API costs by serving cached responses for similar queries.", "tags": ["caching", "cost"]},
]

def mock_embed(text: str, dims: int = 16) -> List[float]:
    vec = [sum(ord(c) * (i + 1) for c in text[:50]) % 1000 / 1000.0 for i in range(dims)]
    norm = math.sqrt(sum(x * x for x in vec)) or 1.0
    return [round(x / norm, 6) for x in vec]

def cosine_sim(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(x * x for x in b))
    return dot / (na * nb) if na and nb else 0.0

# STEP 7: Middleware — request logging
@app.middleware("http")
async def log_requests(request: Request, call_next):
    rid = str(uuid.uuid4())[:8]
    logger.info("-> %s %s [%s]", request.method, request.url.path, rid)
    t0 = time.perf_counter()
    response = await call_next(request)
    ms = (time.perf_counter() - t0) * 1000
    logger.info("<- %s %s %.0fms [%s]", request.method, request.url.path, ms, rid)
    return response

# STEP 8: Global error handler
@app.exception_handler(Exception)
async def global_err(request: Request, exc: Exception):
    logger.error("Unhandled error on %s: %s", request.url.path, exc)
    return JSONResponse(status_code=500, content={"error": "internal_server_error", "detail": str(exc)})

# ── ENDPOINTS ─────────────────────────────────────────────

@app.get("/health", tags=["Health"])
async def health():
    """Health Check — returns service status and timestamp."""
    logger.info("Health check")
    return {
        "status": "healthy",
        "service": "ai_api_service",
        "version": "1.0.0",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "endpoints": ["/health", "/chat", "/embeddings", "/search"],
    }

@app.post("/chat", response_model=ChatResponse, tags=["Chat"])
async def chat(req: ChatRequest):
    """Chat Endpoint — validates messages and returns an AI reply."""
    logger.info("Chat | model=%s messages=%d temp=%.2f", req.model, len(req.messages), req.temperature)
    t0 = time.perf_counter()
    await asyncio.sleep(0.05)

    last = next((m.content for m in reversed(req.messages) if m.role == "user"), "")
    replies = {
        "hello": "Hello! I am your AI assistant. How can I help you today?",
        "fastapi": "FastAPI is excellent for building high-performance AI APIs with automatic validation and async support.",
        "rag": "RAG combines vector search with LLM generation to produce grounded, accurate answers from your documents.",
        "embed": "Embeddings are dense vector representations that capture semantic meaning for similarity search.",
    }
    reply = next((v for k, v in replies.items() if k in last.lower()),
                 "This is a mock AI response. Your request has been processed successfully.")

    ms = (time.perf_counter() - t0) * 1000
    pt = sum(len(m.content.split()) for m in req.messages)
    ct = len(reply.split())
    logger.info("Chat done | tokens_in=%d tokens_out=%d latency=%.1fms", pt, ct, ms)
    return ChatResponse(
        id=f"chat-{uuid.uuid4()}",
        model=req.model,
        created=int(time.time()),
        message=ChatMessage(role="assistant", content=reply),
        usage={"prompt_tokens": pt, "completion_tokens": ct, "total_tokens": pt + ct},
        latency_ms=round(ms, 2),
    )

@app.post("/embeddings", response_model=EmbeddingResponse, tags=["Embeddings"])
async def embeddings(req: EmbeddingRequest):
    """Embeddings Endpoint — converts texts to vectors (max 100 inputs, 8192 chars each)."""
    logger.info("Embeddings | model=%s inputs=%d", req.model, len(req.input))
    t0 = time.perf_counter()
    await asyncio.sleep(0.02)

    dims = 16
    vecs = [mock_embed(t, dims) for t in req.input]
    tok = sum(len(t.split()) for t in req.input)
    ms = (time.perf_counter() - t0) * 1000
    logger.info("Embeddings done | count=%d dims=%d tokens=%d latency=%.1fms", len(vecs), dims, tok, ms)
    return EmbeddingResponse(
        id=f"emb-{uuid.uuid4()}",
        model=req.model,
        embeddings=vecs,
        dimensions=dims,
        token_count=tok,
        latency_ms=round(ms, 2),
    )

@app.post("/search", response_model=SearchResponse, tags=["Search"])
async def search(req: SearchRequest):
    """Search Endpoint — semantic similarity search over the document store."""
    logger.info("Search | query='%s' top_k=%d threshold=%.2f", req.query[:60], req.top_k, req.threshold)
    t0 = time.perf_counter()
    await asyncio.sleep(0.03)

    qv = mock_embed(req.query)
    scored = sorted(
        [(cosine_sim(qv, mock_embed(d["content"])), d) for d in DOCS],
        key=lambda x: x[0], reverse=True
    )
    results = [
        SearchResult(id=d["id"], content=d["content"], score=round(s, 4), metadata={"tags": d["tags"]})
        for s, d in scored[:req.top_k] if s >= req.threshold
    ]
    ms = (time.perf_counter() - t0) * 1000
    logger.info("Search done | results=%d top_score=%.4f latency=%.1fms",
                len(results), results[0].score if results else 0, ms)
    return SearchResponse(
        id=f"srch-{uuid.uuid4()}",
        query=req.query,
        results=results,
        total_found=len(results),
        latency_ms=round(ms, 2),
    )

# STEP 9: Launch
logger.info("=" * 55)
logger.info("  AI API Service starting on http://0.0.0.0:8000")
logger.info("  Interactive docs -> http://0.0.0.0:8000/docs")
logger.info("=" * 55)
uvicorn.run(app, host="0.0.0.0", port=8000, log_level="warning")
