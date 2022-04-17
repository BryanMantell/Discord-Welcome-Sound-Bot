# Import libraries
from ast import And
import discord
import os
import time
import json

# Discord Bot Initialization
client = discord.Client()

# Load JSON File That Stores Token and Save Token To Variable 
with open("config.json") as file:
        config = json.load(file)
Token = config["Token"]

# Assign Discord User IDs
Bryan =  133410206586634240
Michael = 133410284822855680
Mitchell = 233331081376563201
Michiko = 240573911719346177
Stacey = 409561455134769153
Sammy = 210667188917501953
Zubat = 319767910098796544
Akira = 325527466405920770
Brayden = 443375676012101646
Tom = 211332164510285824
Ebi = 791168890788773898
Ramon = 218240244867268618
Matt = 221762697828499456
Micah = 453387223090462732
Sparta = 265285329412423682
Spartan = 239903557808160780

# Create Dictionary of Audio Paths For Player IDs
SoundPath = {"Bryan": "Music\\Ladies.mp3", 
          "Michael": "Music\\Working.mp3",
          "Mitchell": "Music\\Boys.mp3", 
          "Michiko": "Music\\HEYHEY.mp3",
          "Stacey": "Music\\DarkSouls.mp3", 
          "Sammy": "Music\\Hey.mp3",
          "Zubat": "Music\\Hey.mp3", 
          "Akira": "Music\\Hey.mp3",
          "Brayden": "Music\\Hey.mp3", 
          "Tom": "Music\\Hey.mp3",
          "Ebi": "Music\\UWU.mp3", 
          "Ramon": "Music\\Hey.mp3",
          "Matt": "Music\\Knock.mp3", 
          "Micah": "Music\\Hey.mp3",
          "Sparta": "Music\\Hey.mp3",
          "Spartan": "Music\\AHH.mp3"};

# Prepare the Bot for Commands
@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}\nBot is Ready for Use!")

# Play Sound When a User Enters a Voice Channel Based on Their User IDs
@client.event
async def on_voice_state_update(member: discord.Member, before, after):
    vc_before = before.channel
    vc_after = after.channel
    try:
        if vc_before == vc_after:
            return
        if vc_before is None and member.id == Bryan:
            channel = member.voice.channel
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio(SoundPath["Bryan"], executable="ffmpeg\\bin\\ffmpeg.exe"))
            time.sleep(4.5)
            await vc.disconnect()
        if vc_before is None and member.id == Michael:
            channel = member.voice.channel
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio(SoundPath["Michael"], executable="ffmpeg\\bin\\ffmpeg.exe"))
            time.sleep(4)
            await vc.disconnect()
        if vc_before is None and member.id == Mitchell:
            channel = member.voice.channel
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio(SoundPath["Mitchell"], executable="ffmpeg\\bin\\ffmpeg.exe"))
            time.sleep(5)
            await vc.disconnect()
        if vc_before is None and member.id == Michiko:
            channel = member.voice.channel
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio(SoundPath["Michiko"], executable="ffmpeg\\bin\\ffmpeg.exe"))
            time.sleep(4)
            await vc.disconnect()
        if vc_before is None and member.id == Stacey:
            channel = member.voice.channel
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio(SoundPath["Stacey"], executable="ffmpeg\\bin\\ffmpeg.exe"))
            time.sleep(4)
            await vc.disconnect()
        if vc_before is None and member.id == Sammy:
            channel = member.voice.channel
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio(SoundPath["Sammy"], executable="ffmpeg\\bin\\ffmpeg.exe"))
            time.sleep(4)
            await vc.disconnect()
        if vc_before is None and member.id == Zubat:
            channel = member.voice.channel
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio(SoundPath["Zubat"], executable="ffmpeg\\bin\\ffmpeg.exe"))
            time.sleep(4)
            await vc.disconnect()
        if vc_before is None and member.id == Akira:
            channel = member.voice.channel
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio(SoundPath["Akira"], executable="ffmpeg\\bin\\ffmpeg.exe"))
            time.sleep(4)
            await vc.disconnect()
        if vc_before is None and member.id == Brayden:
            channel = member.voice.channel
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio(SoundPath["Brayden"], executable="ffmpeg\\bin\\ffmpeg.exe"))
            time.sleep(4)
            await vc.disconnect()
        if vc_before is None and member.id == Tom:
            channel = member.voice.channel
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio(SoundPath["Tom"], executable="ffmpeg\\bin\\ffmpeg.exe"))
            time.sleep(4)
            await vc.disconnect()
        if vc_before is None and member.id == Ebi:
            channel = member.voice.channel
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio(SoundPath["Ebi"], executable="ffmpeg\\bin\\ffmpeg.exe"))
            time.sleep(4)
            await vc.disconnect()
        if vc_before is None and member.id == Ramon:
            channel = member.voice.channel
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio(SoundPath["Ramon"], executable="ffmpeg\\bin\\ffmpeg.exe"))
            time.sleep(4)
            await vc.disconnect()
        if vc_before is None and member.id == Matt:
            channel = member.voice.channel
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio(SoundPath["Matt"], executable="ffmpeg\\bin\\ffmpeg.exe"))
            time.sleep(4)
            await vc.disconnect()
        if vc_before is None and member.id == Micah:
            channel = member.voice.channel
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio(SoundPath["Micah"], executable="ffmpeg\\bin\\ffmpeg.exe"))
            time.sleep(4)
            await vc.disconnect()
        if vc_before is None and member.id == Sparta:
            channel = member.voice.channel
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio(SoundPath["Sparta"], executable="ffmpeg\\bin\\ffmpeg.exe"))
            time.sleep(4)
            await vc.disconnect()
        if vc_before is None and member.id == Spartan:
            channel = member.voice.channel
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio(SoundPath["Spartan"], executable="ffmpeg\\bin\\ffmpeg.exe"))
            time.sleep(4)
            await vc.disconnect()
    
    except Exception as err:
            print(err)

client.run(Token)
