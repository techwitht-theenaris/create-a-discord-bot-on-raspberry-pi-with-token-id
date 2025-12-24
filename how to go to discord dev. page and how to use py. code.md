
## Step 1: Create Your Application
1. Go to the [Discord Developer Portal](https://discord.com/developers/docs/quick-start/getting-started#step-1-creating-an-app).
2. Click **Create New Application**.
3. Enter your bot’s name and click **Create**.
4. Navigate to the **Bot** tab:
   - Upload an icon for your bot (optional).
   - Scroll down and click **Reset Token** → confirm → enter your email → copy the new token.
   - Save this token securely (e.g., paste it into Notepad).  
     ⚠️ **Never share your token publicly.**

---

## Step 2: Configure Bot Settings
1. In the **Bot** tab, scroll down to **Privileged Gateway Intents**:
   - Enable:
     - Presence Intent  
     - Server Members Intent  
     - Message Content Intent  
2. Scroll further down to **Bot Permissions**:
   - Under **General Permissions**, enable **Administrator** (or select only the permissions your bot needs).

---

## Step 3: Generate OAuth2 URL
1. Go to the **OAuth2** tab.
2. Scroll down to **OAuth2 URL Generator**:
   - Select **bot** and **application.commands**.
   - Under **Bot Permissions**, enable **Administrator** again (or choose specific permissions).
3. Copy the **Generated URL**.
4. Open the URL in your browser.
5. Select the server where you want to add the bot, then click **Authorize**.

---

✅ Your bot is now added to your server! 

Next step (step 4:) go to raspberry pi terminal (can do it any way you can do like ssh)
create a file and other by use this commands ["mkdir" - to create folder "nano" - to create a file "pwd" to look the path that rpi creeut]
1. sudo apt install python3
2. mkdir folder-name
3. nano name-of-file.py
4. paste the code file discord-bot-code.py into the terminal
5. change owen name and discord token id
6. cd folder-name
7. run! use commands (make sure your raspberry pi path it crrect to that folder) python3 name-of-file.py
---

## ⚠️ Important Notes
- Keep your bot token private. If someone else gets it, they can control your bot.
- don't unplug your raspberry pi if you unplug it you can getstart on **6**


 
