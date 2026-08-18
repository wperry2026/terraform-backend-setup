# Import Modules
import json
import boto3
from botocore.exceptions import ClientError

# ANSI Color Codes
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Function to Create S3 Backend Bucket
def create_s3_backend_bucket(bucket_name, region):
    s3_client = boto3.client("s3", region_name=region)

    try:
        # 1. Create Bucket
        if region == "us-east-1":
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={"LocationConstraint": region},
            )
        print(f"✅ S3 Bucket '{bucket_name}' created.")

        # 2. Enable Versioning (Required for state recovery & Object Lock)
        s3_client.put_bucket_versioning(
            Bucket=bucket_name,
            VersioningConfiguration={"Status": "Enabled"},
        )
        print("✅ Versioning enabled.")

        # 3. Enable Server-Side Encryption
        s3_client.put_bucket_encryption(
            Bucket=bucket_name,
            ServerSideEncryptionConfiguration={
                "Rules": [
                    {
                        "ApplyServerSideEncryptionByDefault": {
                            "SSEAlgorithm": "AES256"
                        }
                    }
                ]
            },
        )
        print("✅ Encryption (AES256) enabled.")

        # 4. Block Public Access
        s3_client.put_public_access_block(
            Bucket=bucket_name,
            PublicAccessBlockConfiguration={
                "BlockPublicAcls": True,
                "IgnorePublicAcls": True,
                "BlockPublicPolicy": True,
                "RestrictPublicBuckets": True,
            },
        )
        print("✅ Public access blocked.")

        # 5. Prevent Bucket Deletion
        bucket_policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "PreventBucketDeletion",
                    "Effect": "Deny",
                    "Principal": "*",
                    "Action": "s3:DeleteBucket",
                    "Resource": f"arn:aws:s3:::{bucket_name}",
                }
            ],
        }

        s3_client.put_bucket_policy(
            Bucket=bucket_name,
            Policy=json.dumps(bucket_policy)
        )
        print("✅ DeleteBucket prevention policy attached.")

    except ClientError as e:
            print(f"❌ Error creating S3 bucket: {e}")
    
# Main Execution
if __name__ == "__main__":
    # Prompt for S3 Bucket Name (re-prompts until non-empty value is provided)
    bucket_name = ""
    while not bucket_name:
        bucket_name = input(f"{CYAN}{BOLD}Enter S3 Bucket Name:{RESET} ").strip()
        if not bucket_name:
            print(f"{RED}{BOLD}❌ Bucket name cannot be empty. Please try again.{RESET}")

    # Prompt for AWS Region (re-prompts until non-empty value is provided)
    region = ""
    while not region:
        region = input(f"{CYAN}{BOLD}Enter AWS Region:{RESET} ").strip()
        if not region:
            print(f"{RED}{BOLD}❌ AWS Region cannot be empty. Please try again.{RESET}")

    print(f"\n{YELLOW}{BOLD}🚀 Provisioning S3 Backend Bucket {YELLOW}{BOLD}'{bucket_name}' in '{region}'...{RESET}\n")
    create_s3_backend_bucket(bucket_name, region)