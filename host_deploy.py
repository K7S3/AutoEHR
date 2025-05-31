import requests
import base64

# Your flow ID and endpoint
#url = "http://localhost:7868/api/v1/run/5a760965-fe8a-45b4-9b76-d3d7f3afd266"
url= "http://localhost:7868/api/v1/run/27b7a7f3-0a11-4c90-9374-80b54dd72b15"
# Read and encode the files
with open("Audio_file/audio.mp4", "rb") as f:
    file1_encoded = base64.b64encode(f.read()).decode('utf-8')

with open("PDS_CSVs/blood_work.csv", "rb") as f:
    file2_encoded = base64.b64encode(f.read()).decode('utf-8')

# Construct payload according to your flow input names
payload = {
    "inputs": {
        
        "AssemblyAITranscriptionJobCreator-hh3TP": file1_encoded,  # use the actual node/input names from your flow
        "File-Tt6Uy": file2_encoded,
    }
}

headers = {
    "Content-Type": "application/json"
}

try:
    # Send API request
    response = requests.request("POST", url, json=payload, headers=headers)
    response.raise_for_status()  # Raise exception for bad status codes

    # Print response
    print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
except ValueError as e:
    print(f"Error parsing response: {e}")
    