from discord_bot import PlexBot
from config import PLEX_SERVER_IP, PLEX_TOKEN, DISCORD_TOKEN, CHANNEL_ID, LAST_RUNTIME_FILE, CHECK_INTERVAL


def main():
    bot = PlexBot(
        plex_server_ip=PLEX_SERVER_IP,
        plex_token=PLEX_TOKEN,
        channel_id=CHANNEL_ID,
        runtime_file=LAST_RUNTIME_FILE,
        interval=CHECK_INTERVAL
    )
    bot.run(DISCORD_TOKEN)


if __name__ == "__main__":
    main()
