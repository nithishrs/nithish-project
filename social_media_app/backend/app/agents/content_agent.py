from .config import get_model
import json

class ContentOptimizationAgent:
    def __init__(self):
        self.model = get_model()

    def optimize(self, text: str, platform: str):
        prompt = f"""
        Act as a professional Social Media Manager.
        Optimize the following content for {platform}.
        
        Original Content: "{text}"
        
        Rules:
        - Adjust tone to suit {platform} (e.g., Professional for LinkedIn, Casual for Twitter).
        - Add 3-5 relevant hashtags.
        - Ensure length is appropriate.
        - Give an Optimization Score (1-10) based on engagement potential.
        - Explain what you changed.

        Return valid JSON format:
        {{
            "optimized_text": "string",
            "hashtags": ["list", "of", "strings"],
            "score": integer,
            "explanation": "string"
        }}
        """
        
        try:
            response = self.model.generate_content(prompt)
            # Cleanup json if needed (sometimes model adds backticks)
            cleaned = response.text.replace("```json", "").replace("```", "")
            return json.loads(cleaned)
        except Exception as e:
            return {
                "optimized_text": text,
                "hashtags": [],
                "score": 0,
                "explanation": f"AI Error: {str(e)}"
            }

optimization_agent = ContentOptimizationAgent()
