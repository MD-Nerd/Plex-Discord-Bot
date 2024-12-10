import discord
import requests
from io import BytesIO
import asyncio
from plex import get_recently_added, extract_media_items
from runtime_cache import get_last_runtime, save_current_runtime


class PlexBot(discord.Client):
    def __init__(self, plex_server_ip, plex_token, channel_id, runtime_file, interval):
        super().__init__()
        self.plex_server_ip = plex_server_ip
        self.plex_token = plex_token
        self.channel_id = channel_id
        self.runtime_file = runtime_file
        self.interval = interval

    async def on_ready(self):
        print(f"Logged in as {self.user}")
        channel = self.get_channel(self.channel_id)
        self.loop.create_task(self.check_recently_added(channel))

    async def send_thumbnail_embed(self, channel, media_info):
        """Send an embed with the media info."""
        thumbnail_url = media_info["thumbnail_url"]
        response = requests.get(thumbnail_url)
        if response.status_code == 200:
            image_data = BytesIO(response.content)
            file = discord.File(image_data, filename="thumbnail.jpg")
            embed = discord.Embed(
                title=media_info["title"],
                description=media_info["summary"],
                color=discord.Color.blue()
            )
            embed.add_field(name="Media Type", value=media_info["media_type"], inline=True)
            embed.add_field(name="Year Released", value=media_info["year_released"], inline=True)
            embed.add_field(name="Year Added", value=media_info["year_added"], inline=True)
            embed.set_image(url="attachment://thumbnail.jpg")
            await channel.send(embed=embed, file=file)
        else:
            await channel.send(f"Failed to fetch thumbnail for {media_info['title']}.")

    async def check_recently_added(self, channel):
        """Check for new media periodically."""
        while True:
            print(f"Checking for new media...")
            xml_data = get_recently_added(self.plex_server_ip, self.plex_token)
            if xml_data:
                media_items = extract_media_items(xml_data, self.plex_server_ip, self.plex_token)
                last_runtime = get_last_runtime(self.runtime_file)
                new_media = [item for item in media_items if item["addedAt"] > last_runtime]

                if new_media:
                    for media_info in new_media:
                        await self.send_thumbnail_embed(channel, media_info)
                else:
                    print("No new media found.")
                save_current_runtime(self.runtime_file)
            else:
                print("Failed to retrieve media data.")
            await asyncio.sleep(self.interval)
