
# AutoGen Fundamentals

class UserProxyAgent:

    def send_request(self):
        return "Create a Software Requirement Specification for an AI Helpdesk System."


class AssistantAgent:

    def generate_response(self, request):

        srs = f"""
# Software Requirement Specification

## Project Title
AI Helpdesk System

## Introduction

The AI Helpdesk System is designed to automate customer support using
Artificial Intelligence technologies.

## Objectives

- Automate customer query handling
- Improve response times
- Reduce operational costs
- Provide 24/7 support

## Functional Requirements

1. User Authentication
2. Ticket Management
3. AI Chat Support
4. Knowledge Base Search
5. Report Generation

## Non-Functional Requirements

- Scalability
- Security
- Reliability
- Performance

## Technologies

- Python
- AI Models
- Database Systems
- Cloud Infrastructure
"""

        return srs


class ReviewerAgent:

    def review_response(self, document):

        improvements = """

## Review Comments

- Requirements are clearly defined.
- Functional requirements are complete.
- Non-functional requirements address scalability and security.
- Document structure follows standard SRS format.

## Improved Version Status

Approved with minor enhancements.
"""

        return document + improvements


# Workflow

print("Workflow")
print("User Proxy Agent")
print("       ↓")
print("Assistant Agent")
print("       ↓")
print("Reviewer Agent")
print("       ↓")
print("Improved Response")

# Step 1
user_agent = UserProxyAgent()
request = user_agent.send_request()

# Step 2
assistant_agent = AssistantAgent()
draft_srs = assistant_agent.generate_response(request)

# Step 3
reviewer_agent = ReviewerAgent()
final_srs = reviewer_agent.review_response(draft_srs)

# Save output

with open("Software_Requirement_Specification.md", "w", encoding="utf-8") as f:
    f.write(final_srs)

print("\nSoftware_Requirement_Specification.md generated successfully")
