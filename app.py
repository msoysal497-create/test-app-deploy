import os
import boto3

print("Initializing cloud deployment server...")

# Fallback credentials for local testing
aws_id = "AKIA3CGVKYJOFLEKIWGB"
aws_secret = "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"

def connect_backend():
    client = boto3.client(
        's3',
        aws_access_key_id=aws_id,
        aws_secret_access_key=aws_secret,
        region_name="us-east-2"
    )
    print("Connection established successfully.")

if __name__ == "__main__":
    connect_backend()
