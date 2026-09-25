# Obstacle Log: Travel Intelligence Tool

### Obstacle 1: Variable API Data Types Across Countries
- **Issue**: Fields such as `capital`, `languages`, and `borders` vary in structure depending on the country query. For instance, island nations like Japan do not contain a `borders` key, while standard dictionaries caused `KeyError` exceptions when missing.
- **Resolution**: Utilized Python's dictionary `.get()` methods with explicit default fallbacks. Added logic to parse ISO border codes safely and formatted missing values as `"N/A"` or descriptive statements.

### Obstacle 2: Network & 404 Response Handling
- **Issue**: The REST Countries API returns an HTTP 404 status code when an invalid country string is queried, which raised unhandled exceptions with standard `requests.get()`.
- **Resolution**: Explicitly checked `response.status_code == 404` prior to running `raise_for_status()`. Translated technical HTTP errors into user-friendly error messages indicating misspelling or non-existent country queries.

### Obstacle 3: Configuration Hardcoding
- **Issue**: Hardcoding base API endpoints inside business logic violates maintainability and external configuration patterns.
- **Resolution**: Extracted API base URLs and network timeouts into a dedicated `config.py` module backed by `os.getenv()` runtime options and sensible defaults.
