class MarketplaceSDKException(Exception):
    """Base exception for all Marketplace SDK errors."""
    pass

class MarketplaceAPIError(MarketplaceSDKException):
    """Exception for API errors (HTTP errors, etc)."""
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
        super().__init__(f"API Error {status_code}: {message}")

class MarketplaceConfigError(MarketplaceSDKException):
    """Exception for configuration errors."""
    pass 