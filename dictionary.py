import requests
import json

# Replace with actual Cambridge API details
api_url = "https://dictionary.cambridge.org/api/v1/dictionaries/british/"
word_to_search = "python"

try:
    response = requests.get(api_url, params={"q": word_to_search})
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
    data = response.json()

    # Process the JSON data
    print(json.dumps(data, indent=2))  # Pretty print the JSON

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
