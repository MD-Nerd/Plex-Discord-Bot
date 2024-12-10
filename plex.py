import requests
import xml.etree.ElementTree as ET
from datetime import datetime


def get_recently_added(plex_server_ip, plex_token):
    """Fetch recently added media from Plex."""
    url = f"http://{plex_server_ip}:32400/library/recentlyAdded?X-Plex-Token={plex_token}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error: Unable to query Plex API (Status code: {response.status_code})")
        return None


def extract_media_items(xml_data, plex_server_ip, plex_token):
    """Extract media items from the Plex XML response."""
    root = ET.fromstring(xml_data)
    media_items = []
    for media in root.findall('./Video'):
        title = media.get('title', 'Unknown')
        media_type = media.get('type', 'Unknown')
        summary = media.get('summary', 'No summary available')
        year_released = media.get('year', 'Unknown')
        added_timestamp = media.get('addedAt')
        year_added = datetime.fromtimestamp(int(added_timestamp)).strftime('%Y-%m-%d') if added_timestamp else 'Unknown'
        thumb_path = media.get('thumb')
        thumbnail_url = f"http://{plex_server_ip}:32400{thumb_path}?X-Plex-Token={plex_token}" if thumb_path else None

        media_items.append({
            "title": title,
            "media_type": media_type,
            "summary": summary,
            "year_released": year_released,
            "year_added": year_added,
            "addedAt": int(added_timestamp) if added_timestamp else 0,
            "thumbnail_url": thumbnail_url
        })
    return media_items
