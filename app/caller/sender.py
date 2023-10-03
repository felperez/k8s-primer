from fastapi import FastAPI
import requests

# Create a FastAPI instance
app = FastAPI()

# Define the endpoint to call the other app's "hello" endpoint
@app.get("/call_hello")
def call_hello():
    # URL of the other app's "hello" endpoint
    hello_url = "http://other-app-host:other-app-port/hello"

    try:
        # Make the GET request to the other app's endpoint
        response = requests.get(hello_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            return response.text
        else:
            return f"Failed to call 'hello' endpoint. Status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Error calling 'hello' endpoint: {e}"

# Run the FastAPI app with uvicorn server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
