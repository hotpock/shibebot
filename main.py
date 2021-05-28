import discord
import shibe_api


client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('&shibe'):
        shibe = shibe_api.get_shibe()
        print(shibe)
        shiba = str(shibe)[1:-1]
        print(shiba)
        shiba2 = shiba.strip("'")
        print(shiba2)
        if shibe == False:
            await message.channel.send("Couldn't get shibe. Try again later.")
        else:
            await message.channel.send(shiba2)

client.run('ODQ3ODg3NTcwNzcxOTAyNDg0.YLEm1Q.UbYITqcNv-RIvcvKMV6LV1I6GQs')