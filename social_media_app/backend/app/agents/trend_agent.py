from .config import get_model
import json

class TrendAnalysisAgent:
    def __init__(self):
        self.model = get_model()

    def analyze_trends(self, platform: str):
        prompt = f"""
        Act as a Viral Content Strategist.
        Idenfity current trending topics and content ideas for {platform}.
        Can be general or generic if no live data access, but base it on evergreen + current seasonal trends.
        
        Return valid JSON format:
        {{
            "platform": "{platform}",
            "trends": ["list of trending topics"],
            "hashtags": ["list of specific trending hashtags"],
            "content_ideas": ["3 specific content ideas based on these trends"]
        }}
        """
        
        try:
            response = self.model.generate_content(prompt)
            cleaned = response.text.replace("```json", "").replace("```", "")
            return json.loads(cleaned)
        except Exception as e:
            return {
                "platform": platform,
                "trends": ["General Tech", "AI", "Remote Work"],
                "hashtags": ["#tech", "#ai"],
                "content_ideas": ["Error fetching trends"]
            }

trend_agent = TrendAnalysisAgent()
