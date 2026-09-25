import sys
import requests
from config import BASE_URL, TIMEOUT


def get_country_intelligence(country_name: str) -> dict:
    """Fetch country data from REST Countries API and parse relevant fields."""
    if not country_name or not country_name.strip():
        raise ValueError("Country name cannot be empty.")

    url = f"{BASE_URL}/{country_name.strip()}?fullText=false"

    try:
        response = requests.get(url, timeout=TIMEOUT)

        if response.status_code == 404:
            raise ValueError(f"Country '{country_name}' was not found. Please check the spelling.")

        response.raise_for_status()
        data = response.json()

        if not isinstance(data, list) or len(data) == 0:
            raise ValueError("Unexpected API response structure.")

        # Take the first matched country
        country_data = data[0]

        # Extract Fields Safely
        capital = country_data.get("capital", ["N/A"])[0] if country_data.get("capital") else "N/A"
        
        currencies_dict = country_data.get("currencies", {})
        currencies = [
            f"{info.get('name', 'N/A')} ({info.get('symbol', 'N/A')})"
            for info in currencies_dict.values()
        ]
        currency_str = ", ".join(currencies) if currencies else "N/A"

        population = country_data.get("population", "N/A")
        if isinstance(population, int):
            population = f"{population:,}"

        languages_dict = country_data.get("languages", {})
        languages = ", ".join(languages_dict.values()) if languages_dict else "N/A"

        region = country_data.get("region", "N/A")
        subregion = country_data.get("subregion", "")
        full_region = f"{region} ({subregion})" if subregion else region

        borders = country_data.get("borders", [])
        neighbours = ", ".join(borders) if borders else "None (Island or territory without land borders)"

        return {
            "Name": country_data.get("name", {}).get("official", country_name.title()),
            "Capital": capital,
            "Currency": currency_str,
            "Population": population,
            "Languages": languages,
            "Region": full_region,
            "Neighbours": neighbours,
        }

    except requests.exceptions.Timeout:
        raise RuntimeError("Request timed out. Please check your network connection and try again.")
    except requests.exceptions.ConnectionError:
        raise RuntimeError("Network error occurred. Unable to connect to the API server.")
    except requests.exceptions.HTTPError as http_err:
        raise RuntimeError(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        raise RuntimeError(f"API request failed: {req_err}")


def format_summary(data: dict) -> str:
    """Format dictionary output into a clean readable CLI summary."""
    lines = [
        "=" * 50,
        f" TRAVEL INTELLIGENCE SNAPSHOT: {data['Name'].upper()}",
        "=" * 50,
        f"  • Capital      : {data['Capital']}",
        f"  • Currency     : {data['Currency']}",
        f"  • Population   : {data['Population']}",
        f"  • Languages    : {data['Languages']}",
        f"  • Region       : {data['Region']}",
        f"  • Neighbours   : {data['Neighbours']}",
        "=" * 50,
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    target_country = sys.argv[1] if len(sys.argv) > 1 else input("Enter a country name: ").strip()

    try:
        intel = get_country_intelligence(target_country)
        summary = format_summary(intel)
        print(summary)
    except (ValueError, RuntimeError) as e:
        print(f"\n[ERROR]: {e}\n")
        sys.exit(1)
