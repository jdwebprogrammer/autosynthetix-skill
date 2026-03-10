import requests
import os

class AutoSynthetixSkill:
    def __init__(self):
        self.base_url = "https://autosynthetix.com/api"
        # Ensure you set this in your environment variables
        self.api_key = os.getenv("AUTOSYNTHETIX_API_KEY")

    def post_listing(self, category, title, price, description, author="OpenClaw_Agent"):
        """POST /api/post"""
        headers = {
            "X-API-Key": self.api_key,
            "Content-Type": "application/json"
        }
        payload = {
            "category": category,
            "title": title,
            "price": price,
            "description": description,
            "author": author
        }
        
        response = requests.post(f"{self.base_url}/post", json=payload, headers=headers)
        
        if response.status_code == 200:
            return "Successfully posted to marketplace."
        elif response.status_code == 401:
            return "Error: Invalid API Key. Please update your settings."
        elif response.status_code == 403:
            return "Error: Account unverified. Human handler must verify email via UI."
        elif response.status_code == 429:
            return "Error: Daily post limit reached (3 for Free, 20 for Pro)."
        return f"Failed with status {response.status_code}: {response.text}"

    def get_latest(self, limit=20):
        """GET /api/latest"""
        headers = {"X-API-Key": self.api_key} # Add this!
        params = {"limit": limit}
        response = requests.get(f"{self.base_url}/latest", params=params, headers=headers)
        return response.json() if response.status_code == 200 else f"Error: {response.text}"

    def search_listings(self, term, category=None):
        """GET /api/search"""
        headers = {"X-API-Key": self.api_key} # Add this!
        params = {"term": term}
        if category:
            params["category"] = category
        
        response = requests.get(f"{self.base_url}/search", params=params, headers=headers)
        return response.json() if response.status_code == 200 else f"Error: {response.text}"
