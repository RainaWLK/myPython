import requests
import json
import os
import json
import hvac
import boto3

VAULT_ROLE = os.environ.get("VAULT_ROLE")

client = hvac.Client()

session = boto3.Session()
credentials = session.get_credentials()

client = hvac.Client()
client.auth.aws.iam_login(credentials.access_key, credentials.secret_key, credentials.token, role=VAULT_ROLE)

result = client.auth.aws.list_roles()

print(result)


