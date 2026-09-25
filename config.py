import os

# Base API URL for REST Countries API v3.1
BASE_URL = os.getenv("COUNTRY_API_URL", "https://restcountries.com/v3.1/name")

# HTTP Request Timeout in seconds
TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "10"))
