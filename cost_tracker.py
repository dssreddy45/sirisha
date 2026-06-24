
from datetime import datetime

class CostTracker:

    def __init__(self):
        self.costs = {
            "llm_cost": 45.50,
            "embedding_cost": 12.75,
            "vector_search_cost": 8.20,
            "agent_execution_cost": 15.30
        }

    def calculate_total_cost(self):
        return sum(self.costs.values())

    def generate_report(self):

        total_cost = self.calculate_total_cost()

        report = f'''
# Daily Cost Report

Date: {datetime.now()}

## Cost Breakdown

| Component | Cost ($) |
|------------|-----------|
| LLM Costs | {self.costs["llm_cost"]} |
| Embedding Costs | {self.costs["embedding_cost"]} |
| Vector Search Costs | {self.costs["vector_search_cost"]} |
| Agent Execution Costs | {self.costs["agent_execution_cost"]} |
| Total Cost | {total_cost} |

## Optimization Suggestions

1. Use smaller LLM models for simple tasks.
2. Reduce prompt length to minimize token usage.
3. Cache embedding vectors.
4. Optimize vector search retrieval.
5. Reuse agent outputs where possible.
6. Monitor high-cost workflows regularly.

## Summary

The AI system cost has been analyzed successfully.
Monitoring helps reduce expenses and improve efficiency.
'''

        with open("daily_cost_report.md", "w") as f:
            f.write(report)

        print("daily_cost_report.md generated successfully")

        return report


if __name__ == "__main__":

    tracker = CostTracker()

    print("\n=== Cost Breakdown ===")

    for component, cost in tracker.costs.items():
        print(f"{component}: ${cost}")

    print(f"\nTotal Cost: ${tracker.calculate_total_cost()}")

    tracker.generate_report()
