from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "20824282"))
API_HASH = getenv("API_HASH", "5c49d99b5bb9e41c9b8ada4f826989ef")

BOT_TOKEN = getenv("BOT_TOKEN", "7439639831:AAGVCRa7TNt5Gh5vhw2FRNeFubTHeA-w6qI")
OWNER_ID = int(getenv("OWNER_ID", "7044783841"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://kurt67143:nays@cluster0.vjg7bma.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
MUST_JOIN = getenv("MUST_JOIN", "gecemavisisohbett")
