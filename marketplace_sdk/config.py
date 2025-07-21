import os
from typing import Optional
from .exceptions import MarketplaceConfigError

class MarketplaceConfig:
    def __init__(self, base_url: Optional[str] = None, api_key: Optional[str] = None, timeout: int = 10):
        self.base_url = base_url or os.getenv("MARKETPLACE_BASE_URL")
        self.api_key = api_key or os.getenv("MARKETPLACE_API_KEY")
        self.timeout = timeout
        if not self.base_url:
            raise MarketplaceConfigError("Base URL must be provided via constructor or MARKETPLACE_BASE_URL env var.")

    def get_headers(self) -> dict:
        headers = {"accept": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        return headers 