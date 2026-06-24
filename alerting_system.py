
from datetime import datetime

class AlertingSystem:

    def __init__(self):

        self.metrics = {
            "error_rate": 0.08,
            "daily_cost": 150,
            "service_status": "DOWN",
            "latency_ms": 3500,
            "retrieval_success": False
        }

        self.alerts = []

    def detect_incidents(self):

        if self.metrics["error_rate"] > 0.05:
            self.alerts.append("HIGH ERROR RATE")

        if self.metrics["daily_cost"] > 100:
            self.alerts.append("HIGH COST")

        if self.metrics["service_status"] != "UP":
            self.alerts.append("SERVICE DOWNTIME")

        if self.metrics["latency_ms"] > 2000:
            self.alerts.append("SLOW RESPONSE TIMES")

        if not self.metrics["retrieval_success"]:
            self.alerts.append("FAILED RETRIEVALS")

    def send_email_alert(self):
        print("Email Alert Sent")

    def send_slack_alert(self):
        print("Slack Alert Sent")

    def send_teams_alert(self):
        print("Teams Alert Sent")

    def generate_report(self):

        report = f"""
# Incident Report

Generated: {datetime.now()}

## Detected Incidents

"""

        for alert in self.alerts:
            report += f"- {alert}\n"

        report += """

## Alert Channels

- Email
- Slack
- Microsoft Teams

## Recommended Actions

1. Investigate API failures.
2. Review infrastructure health.
3. Optimize AI model costs.
4. Improve response latency.
5. Verify retrieval pipeline.

## Status

Incident Detection Completed.
"""

        with open("incident_report.md", "w") as f:
            f.write(report)

        print("incident_report.md generated successfully")

if __name__ == "__main__":

    system = AlertingSystem()

    system.detect_incidents()

    print("\nDetected Alerts:")
    for alert in system.alerts:
        print("-", alert)

    system.send_email_alert()
    system.send_slack_alert()
    system.send_teams_alert()

    system.generate_report()
