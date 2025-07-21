import requests
from typing import Optional, Dict, Any
from .config import MarketplaceConfig
from .exceptions import MarketplaceAPIError
from .utils import retry_on_exception, get_logger

class MarketplaceClient:
    def __init__(self, base_url: Optional[str] = None, api_key: Optional[str] = None, timeout: int = 10, log_level: int = None):
        self.config = MarketplaceConfig(base_url=base_url, api_key=api_key, timeout=timeout)
        self.logger = get_logger(level=log_level) if log_level is not None else get_logger()
        self.timeout = timeout

    @retry_on_exception(max_retries=3, delay=1.0, exceptions=(requests.RequestException,))
    def register_agent(self, agent_name: str, agent_url: str, server_url: Optional[str] = None) -> Dict[str, Any]:
        url = server_url or f"{self.config.base_url}/agents/"
        payload = {"agentName": agent_name, "agentUrl": agent_url}
        headers = self.config.get_headers()
        headers["Content-Type"] = "application/json"
        self.logger.info(f"Registering agent '{agent_name}' at '{agent_url}' to '{url}'")
        try:
            response = requests.post(url, json=payload, headers=headers, timeout=self.timeout)
            if not response.ok:
                raise MarketplaceAPIError(response.status_code, response.text)
            return response.json()
        except requests.RequestException as e:
            self.logger.error(f"Failed to register agent: {e}")
            raise

    @retry_on_exception(max_retries=3, delay=1.0, exceptions=(requests.RequestException,))
    def discover_agents(self, server_url: Optional[str] = None) -> Dict[str, Any]:
        url = server_url or f"{self.config.base_url}/agents/"
        headers = self.config.get_headers()
        self.logger.info(f"Discovering agents from '{url}'")
        try:
            response = requests.get(url, headers=headers, timeout=self.timeout)
            if not response.ok:
                raise MarketplaceAPIError(response.status_code, response.text)
            return response.json()
        except requests.RequestException as e:
            self.logger.error(f"Failed to discover agents: {e}")
            raise

    @retry_on_exception(max_retries=3, delay=1.0, exceptions=(requests.RequestException,))
    def request_agent(self, agent_name: str, user_input: str, server_url: Optional[str] = None) -> Dict[str, Any]:
        url = server_url or f"{self.config.base_url}/agents/"
        payload = {"agentFlag": agent_name, "userInput": user_input}
        headers = self.config.get_headers()
        headers["Content-Type"] = "application/json"
        self.logger.info(f"Requesting agent '{agent_name}' with input '{user_input}' at '{url}'")
        try:
            response = requests.post(url, json=payload, headers=headers, timeout=self.timeout)
            if not response.ok:
                raise MarketplaceAPIError(response.status_code, response.text)
            return response.json()
        except requests.RequestException as e:
            self.logger.error(f"Failed to request agent: {e}")
            raise 