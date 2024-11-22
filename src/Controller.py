import os
import requests
from requests_auth_aws_sigv4 import AWSSigV4
import boto3

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
        print("Entered aws credentials os block")
        aws_access_key = os.environ.get("AWS_ACCESS_KEY_ID")
        aws_secret_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
        aws_session_token = os.environ.get("AWS_SESSION_TOKEN")
        print("Exit aws credentials os block")
        aws_region = "ap-south-1"
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
        print("access key",aws_access_key == None, aws_access_key[0])
        print("\n\n")
        print("secret_key",aws_secret_key == None, aws_secret_key[0])
        print("\n\n")
        print("session_key",aws_session_token == None, aws_secret_key[0])
        
        print("Entered session block")
        session = boto3.Session(
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
            aws_session_token=aws_session_token
        )
        print("Exit session block")

        print(session)
        print("Enter sigv4 auth block")
        sigv4_auth = AWSSigV4(service="execute-api", region=aws_region, session=session)
        print("Exit sigv4 auth block")
        url = "https://5iwo7o78b2.execute-api.ap-south-1.amazonaws.com/test/putData"
        response = requests.post(url, json=body, auth=sigv4_auth)
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
