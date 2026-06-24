
from crewai import Agent, Task, Crew, Process

# Research Agent
research_agent = Agent(
    role="Research Agent",
    goal="Collect information and validate sources about the AI industry",
    backstory="Expert researcher specializing in AI market trends and technology developments.",
    verbose=True
)

# Writer Agent
writer_agent = Agent(
    role="Writer Agent",
    goal="Generate reports and summarize research findings",
    backstory="Professional report writer experienced in technical and business reporting.",
    verbose=True
)

# Research Task
research_task = Task(
    description="""
    Research the AI industry.
    
    Responsibilities:
    - Collect information
    - Validate sources
    - Identify major trends
    - Gather market insights
    """,
    expected_output="Detailed research findings about the AI industry.",
    agent=research_agent
)

# Writing Task
writing_task = Task(
    description="""
    Create a professional AI Industry Report based on the research findings.

    Responsibilities:
    - Generate report
    - Summarize findings
    - Present key insights
    """,
    expected_output="Complete AI Industry Report.",
    agent=writer_agent
)

# Workflow
crew = Crew(
    agents=[research_agent, writer_agent],
    tasks=[research_task, writing_task],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff()

print("\n===== AI INDUSTRY REPORT =====\n")
print(result)

with open("AI_Industry_Report.md", "w", encoding="utf-8") as f:
    f.write(str(result))

print("\nAI_Industry_Report.md generated successfully")
