import os
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")
MUST_JOIN = os.getenv("MUST_JOIN")
AUTH_USERS = os.environ.get("AUTH_USERS")
GROUP_ID = os.environ.get("-1001615594988")
OWNER_ID = list({int(x) for x in os.environ.get("OWNER_ID", "").split()})
