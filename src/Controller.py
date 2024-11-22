import os
import requests
from requests_auth_aws_sigv4 import AWSSigV4
import boto3
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
from botocore.credentials import AssumeRoleWithWebIdentityCredentialFetcher, CredentialResolver, create_credential_resolver
import json


def get_aws_credentials(role_arn: str):
    """
    Fetch temporary AWS credentials by assuming the specified role using OIDC.
    """
    session = boto3.Session()
    sts_client = session.client('sts')

    # Assume the specified role using OIDC
    response = sts_client.assume_role(
        RoleArn=role_arn,
        RoleSessionName='github-oidc-session'
    )

    return response['Credentials']



def sign_request(url, method, payload, region, service, aws_credentials):
    """
    Sign the API Gateway request with AWS SigV4 authentication.
    """
    headers = {'Content-Type': 'application/json'}
    request = AWSRequest(
        method=method.upper(),
        url=url,
        data=json.dumps(payload),
        headers=headers
    )

    # Perform SigV4 signing
    SigV4Auth(
        credentials=aws_credentials,
        service_name=service,
        region_name=region
    ).add_auth(request)

    return request


def invoke_api(url, method, payload, aws_credentials):
    """
    Invoke the API Gateway endpoint with AWS SigV4-signed headers.
    """
    signed_request = sign_request(
        url=url,
        method=method,
        payload=payload,
        region="ap-south-1",  # Update to your region
        service="execute-api",
        aws_credentials=aws_credentials
    )

    # Send the signed request using `requests`
    response = requests.request(
        method=signed_request.method,
        url=signed_request.url,
        headers=dict(signed_request.headers),
        data=signed_request.body
    )

    return response





def putData(name, branch, url, languages, is_private, now):
    print("hello")
    username, reponame = name.split('/')
    body = {
        "username": username,
        "reponame": reponame,
        "branch": branch,
        "url": url,
        "languages": languages,
        "lastUpdated": str(now),
        "is_private": is_private
    }

    
    try:
        # print("Entered aws credentials os block")
        # aws_access_key = os.environ.get("AWS_ACCESS_KEY_ID")
        # aws_secret_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
        # aws_session_token = os.environ.get("AWS_SESSION_TOKEN")
        # print("Exit aws credentials os block")
        # aws_region = "ap-south-1"
        # For local 
        # client = boto3.client("sts")
        # response = client.get_session_token(
        #     DurationSeconds=900,
        #     SerialNumber='MFASerialNumber',
        #     TokenCode='string'
        # )
        # print(response)
        # aws_access_key = response['Credentials']['AccessKeyId']
        # aws_secret_key = response['Credentials']['SecretAccessKey']
        # aws_session_token = response['Credentials']['SessionToken']
        # print("access key",aws_access_key == None, aws_access_key[0])
        # print("\n\n")
        # print("secret_key",aws_secret_key == None, aws_secret_key[0])
        # print("\n\n")
        # print("session_key",aws_session_token == None, aws_secret_key[0])
        
        # print("Entered session block")
        # session = boto3.Session(
        #     aws_access_key_id=aws_access_key,
        #     aws_secret_access_key=aws_secret_key,
        #     aws_session_token=aws_session_token
        # )
        # print("Exit session block")

        # print(session)
        # print("Enter sigv4 auth block")
        # sigv4_auth = AWSSigV4(service="execute-api", region=aws_region, session=session)
        # print("Exit sigv4 auth block")




        
        url = "https://5iwo7o78b2.execute-api.ap-south-1.amazonaws.com/test/putData"


        http_method = "POST"
        role_arn = os.environ.get("ROLE_ARN")

        print("Step 1: Start")
        # Step 1: Get temporary AWS credentials
        credentials = get_aws_credentials(role_arn)
        print("Step 1: End")

        print("Step 2: Start")

        # Step 2: Convert credentials for SigV4 signing
        aws_credentials = boto3.Session(
            aws_access_key_id=credentials['AccessKeyId'],
            aws_secret_access_key=credentials['SecretAccessKey'],
            aws_session_token=credentials['SessionToken']
        ).get_credentials()
        print("Step 2: End")

        print("Step 3: Start")
        # Step 3: Call the API Gateway
        response = invoke_api(url, http_method, body, aws_credentials)
        print("Step 3: End")

        if response.status_code == 200:
            print(f"Successfully Put data with username: {username}, reponame: {reponame}")
            return True
        else:
            print(response.status_code)
            print("\n\n")
            print("response body:", response.content)
            print("AWS Internal Error")
            return False
    except Exception as exc:
        print(f"Exception: {exc}")
        return False
