from .config import get_model
import json
from datetime import datetime

class TimingResearchAgent:
    def __init__(self):
        self.model = get_model()

    def get_best_times(self, platform: str, timezone: str):
        prompt = f"""
        Act as a Social Media Analyst.
        Identify the best times to post on {platform} for a user in {timezone} timezone.
        Aggregate data from general best practices (e.g., Hootsuite, SproutSocial stats knowledge).
        
        Return valid JSON format:
        {{
            "platform": "{platform}",
            "timezone": "{timezone}",
            "best_times": ["Day Time format", "e.g. Monday 10:00 AM"],
            "reasoning": "Brief explanation of why these times work."
        }}
        """
        
        try:
            response = self.model.generate_content(prompt)
            cleaned = response.text.replace("```json", "").replace("```", "")
            return json.loads(cleaned)
        except Exception as e:
            return {
                "platform": platform,
                "timezone": timezone,
                "best_times": ["Monday 9:00 AM (Default)"],
                "reasoning": f"AI Error: {str(e)}"
            }

timing_agent = TimingResearchAgent()
