import os

# Load sensitive data from environment variables
PLEX_SERVER_IP = os.getenv("PLEX_SERVER_IP", "localhost")
PLEX_TOKEN = os.getenv("PLEX_TOKEN", "your_plex_token")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN", "your_discord_bot_token")
CHANNEL_ID = int(os.getenv("CHANNEL_ID", "your_discord_channel_ID"))
LAST_RUNTIME_FILE = os.getenv("LAST_RUNTIME_FILE", "last_runtime.txt")
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", 60))
