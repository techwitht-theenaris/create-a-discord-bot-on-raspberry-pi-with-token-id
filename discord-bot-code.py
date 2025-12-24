# bot.py - FINAL VERSION with beautiful /information command
import discord
from discord import app_commands
from discord.ext import commands
import json
import os
from datetime import datetime

OWNER_USERNAME = "your-username" # it use for remember you don't kick (ex. thee0691)
discord-token = "your-discord-token" # discord token you can get form discord dev. page (ex. asdfghjklghjdkslahdfskdjlhjskal)

BAD_WORDS = [
    "fuck", "shit",  # you can remove or add badword here (ex. BAD_WORDS = ["fuck", "shit" , "gay"]
]

WARNINGS_FILE = "warnings.json"

def load_warnings():
    if os.path.exists(WARNINGS_FILE):
        with open(WARNINGS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_warnings(w):
    with open(WARNINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(w, f, indent=4, ensure_ascii=False)

warnings = load_warnings()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot online → {bot.user}")
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} slash commands!")

user_lang = {}

TRANSLATIONS = {
    "en": {
        "hello": "Hello {user}!",
        "bye": "Bye {user} See you!",
        "rules": "**Server Rules**\n• Be respectful\n• No spam\n• No bad words(you get f*** of here if you do this)\n• Have fun!\n•",
        "lang_set": "Language set to English",
        "warn": "you get f*** of here if do this (Warning {count}/3)",
        "kicked": "Kicked for using bad words 3 times"
    },
    "th": {
        "hello": "สวัสดี {user}!",
        "bye": "บายครับ {user} เจอกันใหม่!",
        "rules": "**กฎเซิร์ฟเวอร์**\n• เคารพกัน\n• ห้ามสแปม\n• ห้ามคำหยาบ\n• :)",
        "lang_set": "ตั้งภาษาเป็นไทยแล้ว",
        "warn": "ห้ามพูดคำหยาบ! เตือนครั้งที่ {count}/3",
        "kicked": "ถูกเตะเพราะคำหยาบครบ 3 ครั้ง"
    }
}

def get_lang(uid):
    return user_lang.get(uid, "en")

# Slash commands
@bot.tree.command(name="hello")
async def hello(i: discord.Interaction):
    await i.response.send_message(TRANSLATIONS[get_lang(i.user.id)]["hello"].format(user=i.user.mention))

@bot.tree.command(name="bye")
async def bye(i: discord.Interaction):
    await i.response.send_message(TRANSLATIONS[get_lang(i.user.id)]["bye"].format(user=i.user.mention))

@bot.tree.command(name="rules")
async def rules(i: discord.Interaction):
    await i.response.send_message(TRANSLATIONS[get_lang(i.user.id)]["rules"])

# REAL SERVER INFORMATION COMMAND
@bot.tree.command(name="information", description="Show server information")
async def information(interaction: discord.Interaction):
    guild = interaction.guild
    created = guild.created_at.strftime("%d %B %Y")
    lang = get_lang(interaction.user.id)

    embed = discord.Embed(title=f"{guild.name} Information", color=0x00ffea)
    embed.set_thumbnail(url=guild.icon.url if guild.icon else None)
    embed.add_field(name="Owner", value=guild.owner.mention, inline=True)
    embed.add_field(name="Members", value=guild.member_count, inline=True)
    embed.add_field(name="Created", value=created, inline=True)
    embed.add_field(name="Channels", value=len(guild.text_channels) + len(guild.voice_channels), inline=True)
    embed.add_field(name="Roles", value=len(guild.roles), inline=True)
    embed.add_field(name="Boosts", value=f"{guild.premium_subscription_count} (Level {guild.premium_tier})", inline=True)
    embed.set_footer(text=f"Bot by {OWNER_USERNAME}")

    await interaction.response.send_message(embed=embed)

@app_commands.choices(language=[app_commands.Choice(name="English", value="en"), app_commands.Choice(name="ไทย", value="th")])
@bot.tree.command(name="set-lang")
async def set_lang(i: discord.Interaction, language: app_commands.Choice[str]):
    user_lang[i.user.id] = language.value
    await i.response.send_message(TRANSLATIONS[language.value]["lang_set"])

# Anti bad words
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if any(word in message.content.lower() for word in BAD_WORDS):
        uid = str(message.author.id)
        lang = get_lang(message.author.id)
        warnings[uid] = warnings.get(uid, 0) + 1
        save_warnings(warnings)
        count = warnings[uid]

        try:
            await message.delete()
        except:
            pass

        await message.channel.send(
            f"{message.author.mention} {TRANSLATIONS[lang]['warn'].format(count=count)}",
            delete_after=8
        )

        if count >= 3 and message.author.name.lower() != OWNER_USERNAME.lower():
            try:
                await message.author.kick(reason="Bad words x3")
                await message.channel.send(TRANSLATIONS[lang]["kicked"])
                warnings.pop(uid, None)
                save_warnings(warnings)
            except:
                pass

    await bot.process_commands(message)

# RUN WITH YOUR TOKEN
bot.run(discord-token)
