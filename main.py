import discord
import regex

import data

token = open("token.txt", "r").read()

client = discord.Client()


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    for playlist in data.playlists:
        if regex.match('(play ' + playlist["name"] + '){e<=3}', message.content):
            embed=discord.Embed(color=0x1aa31f)
            embed.add_field(name=playlist["name"], value=f"=p {playlist['url']}", inline=False)
            await message.channel.send(embed=embed)

@client.event
async def on_raw_reaction_add(payload):
    if payload.emoji.name == "🛡️":
        channel = client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        user = message.author.name
        if str(payload.user_id) != "633749005909884929":
            exit()
        words = message.content.split()[1:]
        song = ''.join(f"{c} " for c in words)
        with open("music.txt", "a") as f:
            f.write(f"{song}:{user}\n")
        await message.add_reaction("👌")
        
client.run(token)
