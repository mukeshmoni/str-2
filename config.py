from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "15692563"))
API_HASH = getenv("API_HASH", "03ab15637e799898d233250c731cd114")

BOT_TOKEN = getenv("BOT_TOKEN", "5873474775:AAF3oD8pGtbHt5dJp2QDZO6qt0swoaAdId8")
OWNER_ID = int(getenv("OWNER_ID", "6798074818"))

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://moniee:moniee@cluster0.cei6n.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
MUST_JOIN = getenv("MUST_JOIN", "TMK_MUSICCHANNEL")
