
# AI Agent Architecture Research

## 1. Chatbot vs AI Agent
| Feature | Chatbot | AI Agent |
|---|---|---|
| Function | Answers questions | Performs tasks |
| Behavior | Static | Dynamic |
| Tools | No tools | Tool enabled |
| Actions | Limited | Autonomous |

## 2. AI Agent
A system that perceives, reasons, acts, and iterates to achieve goals.
- Perception: Receives inputs (text, files, APIs)
- Reasoning: LLM decides what to do next
- Action: Calls tools, writes code, browses web
- Feedback Loop: Observes results and adjusts

## 3. Autonomous Agent
Operates independently with minimal human intervention.
- Self-directed, persistent, error-recovering
- Breaks large goals into smaller sub-tasks
- Examples: AutoGPT, BabyAGI, Devin

## 4. Agentic Workflow
Structured loop: Plan → Execute → Observe → Reflect → Repeat
- Sequential, Parallel, Conditional, Iterative, Hierarchical

## 5. Tool Calling
LLM requests external tools to extend its capabilities.
- Web Search, Code Execution, File I/O, APIs, Email

## 6. Function Calling
LLM outputs structured JSON to call defined functions.
- Example: {"name": "get_weather", "arguments": {"city": "Hyderabad"}}

## 7. Planning
Breaking goals into ordered sub-tasks.
- ReAct: Thought → Action → Observation → Answer
- Chain-of-Thought: Step by step reasoning
- Tree of Thoughts: Explore multiple paths, pick best

## 8. Memory
| Type | Description |
|---|---|
| Sensory | Current context window |
| Working | Current task scratch pad |
| Episodic | Past experiences in database |
| Semantic | Facts in vector DB |
| Procedural | Skills in model weights |

## 9. Reflection
Agent evaluates its own output and improves it.
- Self-Critique → Feedback → Revised Output
- Example: Wrong answer detected → Corrected automatically

## 10. Multi-Agent Systems
Multiple agents collaborate on complex problems.
- Orchestrator assigns tasks to worker agents
- Frameworks: AutoGen, CrewAI, LangGraph, MetaGPT
