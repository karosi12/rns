# Create a Django app

Create a Django route that takes a file upload, creates a new key, encrypts the file and stores in S3 (or file system)

---
## Requirements

- Python 3.8+ (Python 3.8 or newer is recommended)
- pip (Python package manager)
- virtualenv (optional, for virtual environment management)

### Setup Instructions
- #### Clone the Repository

      $ python3 -m venv venv
      $ source venv/bin/activate  # On Windows use `venv\Scripts\activate`

- #### Install Project Dependencies

  Install required Python packages from the requirements.txt file.

      $ pip install -r requirements.txt

- #### Set Up Environment Variables

  Create a .env file in the root directory to securely manage environment variables.

        touch .env

 Populate .env with necessary environment variables. Example:

        DEBUG=True
        AWS_ACCESS_KEY_ID='aws_access_key_id'
        AWS_SECRET_ACCESS_KEY='aws_secret_access_key'
        AWS_STORAGE_BUCKET_NAME='rns-bucket-backend'
        AWS_REGION='us-east-1'
        USE_S3='True'

- #### Running the Development Server

    To start the Django development server:

        python manage.py runserver

## Open web browser
    http://127.0.0.1:8000/files/

