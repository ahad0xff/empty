from dotenv import load_dotenv
from os import environ

load_dotenv('config.env', override=True)

UPSTREAM_REPO = environ.get('UPSTREAM_REPO')
UPSTREAM_BRANCH = environ.get('UPSTREAM_BRANCH')

print(UPSTREAM_REPO)
print(UPSTREAM_BRANCH)
