# Plex Discord Bot

A Python bot that fetches recently added media from a Plex server and sends updates to a Discord channel. This bot is modular, easy to configure, and designed for extensibility. Ideal for notifying users about new media added to your Plex library.

---

## **Features**
- Fetches recently added media from a Plex server.
- Sends media details and thumbnails to a Discord channel.
- Avoids duplicates by caching the last runtime.
- Modular design for easy customization and extension.
- Works with environment variables for secure configuration.

---

## **Table of Contents**
1. [Installation](#installation)
2. [Setup](#setup)
3. [Configuration](#configuration)
4. [Usage](#usage)
5. [Modular Structure](#modular-structure)
6. [Contributing](#contributing)

---
![image](https://github.com/user-attachments/assets/4b5cd7e9-e9b6-4c58-b095-3820a96ad613)
---



## **Installation**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/plex-discord-bot.git
   cd plex-discord-bot
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   - Create a `.env` file in the project root:
     ```env
     PLEX_SERVER_IP=localhost
     PLEX_TOKEN=your-plex-token
     DISCORD_TOKEN=your-discord-token
     CHANNEL_ID=1234567890
     LAST_RUNTIME_FILE=last_runtime.txt
     CHECK_INTERVAL=60
     ```

4. **Run the Bot**:
   ```bash
   python main.py
   ```

---

## **Setup**

1. **Plex Server**:
   - Ensure your Plex server is running and accessible.
   - Obtain your Plex Token ([Guide](https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/)).

2. **Discord Bot**:
   - Create a Discord bot at the [Discord Developer Portal](https://discord.com/developers/applications).
   - Obtain your bot token and invite the bot to your server.

3. **Environment Variables**:
   - Store sensitive data in the `.env` file to keep it secure.

---

## **Configuration**

### **Environment Variables**
| Variable           | Description                                  |
|--------------------|----------------------------------------------|
| `PLEX_SERVER_IP`   | IP or domain of your Plex server.            |
| `PLEX_TOKEN`       | Plex authentication token.                  |
| `DISCORD_TOKEN`    | Discord bot token.                          |
| `CHANNEL_ID`       | Discord channel ID for sending updates.     |
| `LAST_RUNTIME_FILE`| Path to cache file for the last runtime.     |
| `CHECK_INTERVAL`   | Time interval (in seconds) between checks.   |

### **Runtime Cache**
- The bot uses `last_runtime.txt` to store the last runtime.
- If the file doesn't exist, it will be created automatically.
- To reset, delete the file and restart the bot.

---

## **Usage**

1. Start the bot:
   ```bash
   python main.py
   ```
2. The bot will:
   - Query your Plex server every `CHECK_INTERVAL` seconds.
   - Send an embed message for each new media item added since the last check.

---

## **Modular Structure**

### **Project Structure**
```
plex-discord-bot/
├── main.py            # Entry point for the bot.
├── discord_bot.py     # Discord bot logic.
├── plex.py            # Plex API interaction.
├── runtime_cache.py   # Cache management.
├── config.py          # Configuration setup.
├── requirements.txt   # Python dependencies.
└── README.md          # Documentation.
```

### **Module Details**

1. **`plex.py`**
   - Handles interaction with the Plex API.
   - Fetches recently added media and parses XML responses.

2. **`runtime_cache.py`**
   - Manages the last runtime cache file.

3. **`discord_bot.py`**
   - Contains all Discord-related logic.
   - Sends embed messages to the specified channel.

4. **`config.py`**
   - Loads environment variables for configuration.

5. **`main.py`**
   - The entry point for starting the bot.
   - Initializes and runs the bot.

---

## **Contributing**

1. **Fork the Repository**:
   - Click the "Fork" button at the top of this page.

2. **Create a New Branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Commit Changes**:
   ```bash
   git commit -m "Add your message here"
   ```

4. **Push Changes**:
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Submit a Pull Request**:
   - Go to your forked repository and click "New Pull Request".

---

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Happy Coding! 🎉

