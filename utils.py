import requests
from config import VAPI_API_KEY, RETELL_API_KEY

def create_agent_vapi(data):
    url = "https://api.vapi.ai/assistant"  # The URL to Vapi API
    headers = {
        "Authorization": f"Bearer {VAPI_API_KEY}",
        "Content-Type": "application/json"
    }

    # Create payload from user data
    payload = {
        "name": data.get("name"),
        "voice": data.get("voice"),
        # "instructions": data.get("instructions")
    }

    # Make POST request to Vapi API
    response = requests.post(url, json=payload, headers=headers)

    # Process response based on the status code
    if response.status_code == 200 or response.status_code == 201:
        json_data = response.json()
        # Return the assistant ID as a plain text message
        return f"Assistant created successfully! Assistant ID: {json_data.get('id', 'N/A')}"
    else:
        # If there is an error, return the error message in plain text
        return f"Error: {response.status_code} - {response.text}"
    

def create_agent_retell(data):
    # Try RetellAI's API with their documented endpoint
    url = "https://api.retell.io/api/create-agent"  # Modified endpoint path
    
    headers = {
        "Authorization": f"Bearer {RETELL_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "name": data.get("name", "Default Agent"),
        "voice_id": data.get("voice", "11labs-Adrian"),
        "model": data.get("model", "gpt-4")
    }

    print(f"Attempting to connect to: {url}")
    
    try:
        # Try with SSL verification disabled (only for testing)
        response = requests.post(url, json=payload, headers=headers, verify=False)
        
        if response.status_code == 200 or response.status_code == 201:
            json_data = response.json()
            return f"RetellAI Agent created successfully! Agent ID: {json_data.get('id', 'N/A')}"
        else:
            return f"Error: {response.status_code} - {response.text}"
    
    except requests.exceptions.SSLError as e:
        return f"SSL Error: {str(e)}\n\nTry checking if the RetellAI API domain is correct."
    except requests.exceptions.ConnectionError as e:
        return f"Connection Error: {str(e)}\n\nTry checking your network settings and the API endpoint."
    except Exception as e:
        return f"Unexpected Error: {str(e)}"