from transformers import AutoModelForCausalLM, AutoTokenizer
import random
import discord
from discord.ext import commands
from discord.ext.commands import Bot

from model_generator import Generator

#model and tokenizer initialization through HuggingFace
tokenizer = AutoTokenizer.from_pretrained('Models/epochs_1/')
model = AutoModelForCausalLM.from_pretrained('Models/epochs_1/')
special_token = '<|endoftext|>'

#Creating a discord bot
client = commands.Bot(command_prefix = '!', help_command = None)

#command executed when the bot first comes online
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="House MD // !help"))

#the first message sent by MedBot when it joins a server
@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            title = "Hello, there!"
            description = "I am MedBot and I have just been invited to this server! type '!help' to know more"
            emb = discord.Embed(title = title, description = description, color = 0xf4fc58)
            await channel.send(embed = emb)
        break

#constantly runs, takes messages from the user and responds using the provided dataset
@client.event
async def on_message(message):
    msg = message.content.strip()
    reply = Generator.get_reply(msg.strip())

    if message.author == client.user:
        return

    if message.content.startswith(msg) and not message.content.startswith('!'):
        await message.channel.send(reply)
    await client.process_commands(message)

    #a log of every conversation is recorded on Logs.txt
    with open('Logs.txt', 'a', encoding = "UTF-8") as f:
        f.write(f'User: {msg}\nMedBot: {reply}\n')

#help command: type "!help" to get more information about the bot
@client.command()
async def help(ctx, *, message = "all"):
    name = "I am the MedBot!"
    text = "I am MedBot! I am trained on medical queries from all over the internet to generate answers to all medical questions you could have. I am trained on a distilled version of GPT-2 and am still a work in progress!"

    emb = discord.Embed(title = name, description = text, color = 0xf4fc58)
    await ctx.send(embed = emb)

client.run('OTQyNzc2ODc3NTExMjMzNTU2.YgpbYw.3mYv43HF1LOIUxd2f0OlcUNxnEI')
