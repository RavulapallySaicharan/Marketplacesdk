from marketplace_sdk import MarketplaceClient

# Initialize the client (using constructor args or environment variables)
client = MarketplaceClient(base_url="http://localhost:5565")

# Register an agent
try:
    response = client.register_agent("Problem Solver Agent 3", "http://0.0.0.0:9999")
    print("Register Agent Response:", response)
except Exception as e:
    print("Error registering agent:", e)

# Discover agents
try:
    agents = client.discover_agents()
    print("Discovered Agents:", agents)
except Exception as e:
    print("Error discovering agents:", e)

# Request an agent
try:
    result = client.request_agent("Problem Solver Agent 3", "What is the weather?")
    print("Agent Response:", result)
except Exception as e:
    print("Error requesting agent:", e) 