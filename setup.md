🚀 How to Create and Add a Discord Bot
This guide walks you through creating a Discord bot, configuring its settings, and adding it to your server.

Step 1: Create Your Application
- Go to the Discord Developer Portal.
- Click Create New Application.
- Enter your bot’s name and click Create.
- Navigate to the Bot tab:
- Upload an icon for your bot (optional).
- Scroll down and click Reset Token → confirm → enter your email → copy the new token.
- Save this token securely (e.g., paste it into Notepad).
⚠️ Never share your token publicly.

Step 2: Configure Bot Settings
- In the Bot tab, scroll down to Privileged Gateway Intents:
- Enable:
- Presence Intent
- Server Members Intent
- Message Content Intent
- Scroll further down to Bot Permissions:
- Under General Permissions, enable Administrator (or select only the permissions your bot needs).

Step 3: Generate OAuth2 URL
- Go to the OAuth2 tab.
- Scroll down to OAuth2 URL Generator:
- Select bot and application.commands.
- Under Bot Permissions, enable Administrator again (or choose specific permissions).
- Copy the Generated URL.
- Open the URL in your browser.
- Select the server where you want to add the bot, then click Authorize.

✅ Your bot is now added to your server!
Next step (step 4:) go to raspberry pi terminal (can do it any way you can do like ssh) create a file and other by use this commands ["mkdir" - to create folder "nano" - to create a file "pwd" to look the path that rpi creeut]
- sudo apt install python3
- mkdir folder-name
- nano name-of-file.py
- paste the code file discord-bot-code.py into the terminal
- change owen name and discord token id
- cd folder-name
- run! use commands (make sure your raspberry pi path it crrect to that folder) python3 name-of-file.py

⚠️ Important Notes
- Keep your bot token private. If someone else gets it, they can control your bot.
- don't unplug your raspberry pi if you unplug it you can getstart on **6**
do it angin
