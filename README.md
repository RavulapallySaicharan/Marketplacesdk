# marketplace_sdk

A Python SDK for interacting with the Marketplace platform.

## 📦 Installation

```bash
pip install marketplace_sdk
```

## 🛠️ Setup Instructions

You can configure the SDK using constructor arguments or environment variables:

- `MARKETPLACE_BASE_URL`: The base URL of your Marketplace API (e.g., `http://localhost:5565`)
- `MARKETPLACE_API_KEY`: (Optional) Your API key for authentication

## ⚙️ Usage Example

```python
from marketplace_sdk import MarketplaceClient

# Option 1: Configure via constructor
client = MarketplaceClient(base_url="http://localhost:5565", api_key="your_api_key")

# Option 2: Use environment variables
# export MARKETPLACE_BASE_URL=http://localhost:5565
# export MARKETPLACE_API_KEY=your_api_key
# client = MarketplaceClient()

# Register an agent
response = client.register_agent("Problem Solver Agent 3", "http://0.0.0.0:9999")
print(response)

# Discover agents
agents = client.discover_agents()
print(agents)

# Request an agent
result = client.request_agent("Problem Solver Agent 3", "What is the weather?")
print(result)
```

## 📖 Method Descriptions

### `register_agent(agent_name: str, agent_url: str, server_url: Optional[str] = None) -> dict`
- **Inputs:**
  - `agent_name` (str): Name of the agent
  - `agent_url` (str): URL where the agent is running
  - `server_url` (str, optional): Override the API endpoint
- **Returns:** dict (API response)
- **Raises:** `MarketplaceAPIError`, `MarketplaceConfigError`

### `discover_agents(server_url: Optional[str] = None) -> dict`
- **Inputs:**
  - `server_url` (str, optional): Override the API endpoint
- **Returns:** dict (list of agents)
- **Raises:** `MarketplaceAPIError`, `MarketplaceConfigError`

### `request_agent(agent_name: str, user_input: str, server_url: Optional[str] = None) -> dict`
- **Inputs:**
  - `agent_name` (str): Name of the agent
  - `user_input` (str): Input for the agent
  - `server_url` (str, optional): Override the API endpoint
- **Returns:** dict (API response)
- **Raises:** `MarketplaceAPIError`, `MarketplaceConfigError`

## 🚨 Common Exceptions
- `MarketplaceAPIError`: Raised for HTTP/API errors
- `MarketplaceConfigError`: Raised for configuration issues

## 🧪 Testing

To run tests:

```bash
pip install .[test]
pytest tests/
```

## 🧪 Example Usage
See `examples/example_usage.py` for a full usage example.