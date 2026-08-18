# terraform-backend-setup
Setup a Terraform remote backend using an AWS S3 Bucket to store the Terraform State and Lock Files

We will use Python Boto3 to provision the AWS S3 Bucket.


# Setup Process

1. Install AWS CLI client
    - Open terminal, copy and paste the following and press enter:

        sudo apt update && sudo apt install -y curl unzip
        curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
        unzip awscliv2.zip
        sudo ./aws/install

    - After install completes, type aws --version and press enter

    Note: 'aws-cli/2.33.21 Python/3.13.11 Linux/7.0.0-28-generic exe/x86_64.ubuntu.26' is returned the aws client has been installed

2. Configure AWS Credentials
    - In the terminal, type aws configure and press enter
    - Add the Access Key and the Secret Access Key of the AWS IAM user that will be signed into AWS to make the required changes


3. Create Github Repo
    - Open a web browser and go to github.com
    - Sign into GitHub with username and password
    - Click on Repositories
    - Click on New
    - On the Create A New Repository form:
        - Repository Name: Terraform-Backend-Setup
        - Description: Setup terraform-backend using S3 for state and lock files 
        - Add Readme - Click on switch to turn on
        - Click on Create Repository

4. Clone Repository
    - Click on Repositories
    - Click on Terraform-Backend-Setup
    - Click on Code
    - Under Clone, click on HTTPS and copy the link
    - On the local computer, open a terminal window
    - Type git clone, paste the link and press enter. The link should be git clone https://github.com/wperry2026/terraform-backend-setup.git
    - Type cd terraform-backend-setup and press enter

5. Install Python
    - Type python3 --version press enter
    
    Note: if Python 3.14.4 or similar is returned, then Python is installed

6. Create and Activate Virtual Environment
    - Type python3 -m venv venv and press enter
    - Type source venv/bin/activate and press enter

7. Install Boto3
    - pip install boto3

8. Run the script
    - type setup_backend.py and press enter

    Note: You should see a set of confirmation messages confirming that the S3 bucket has been setup and configured as required. 
