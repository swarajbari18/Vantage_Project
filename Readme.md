# Forex API Integration

This project integrates with the Vantage API to provide real-time and historical foreign exchange (forex) data. Follow the steps below to set up and run the project.

## Setup

### 1. Create a Virtual Environment

Before installing the project dependencies, it's recommended to set up a virtual environment to isolate the dependencies for this project.

```bash
python -m venv venv
```

### 2. Activate that Virtual Environment

For Windows:
```cmd
venv\Scripts\activate
```


For Unix or MacOS:

```bash
source venv/bin/activate
```


### 3. Install Requirements:

```bash
pip install -r requirements.txt
```


### 4. Set Up API Key:

Obtain your API key from Vantage.

Export the API key to the environment:

```bash
export VANTAGE_API_KEY=your_api_key
```

Replace your_api_key with your actual API key.

If you are in windows then use git bash, or set the environment variable from the control panel


### 5. Run the Server

Run the Django development server to start the application:

```bash
python manage.py runserver
```
Visit http://localhost:8000/ in your web browser to access the application.

### Additional Notes

Keep your API key confidential; do not expose it in public repositories.
Make sure the virtual environment is activated whenever you work on this project.
Check the Vantage API documentation for details on available endpoints and functionalities.
Happy coding!