import os
API_ID = int(os.getenv("9049867"))
API_HASH = os.getenv("972c0f2e94973b5ffa9a89cb34e5671b")
BOT_TOKEN = os.getenv("5044581355:AAGq8LYU_Q321_m3iuR3JaSmMyQJufPAFW0")
DATABASE_URL = os.getenv("DATABASE_URL")
OWNER_ID = list({int(x) for x in os.environ.get("1901997764", "").split()})
