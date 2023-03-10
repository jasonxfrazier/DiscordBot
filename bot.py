import discord
import responses


async def send_message(message, user_message, is_private) -> None:
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot() -> None:
    TOKEN: str = "TOKEN HERE"
    intents = discord.Intents.default()
    intents.message_content: bool = True
    client = discord.Client(intents = intents)

    @client.event
    async def on_ready() -> None:
        await client.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.listening, 
                name='/help'
            ))
        print(f'{client.user} is now running')

    @client.event
    async def on_message(message) -> None:
        if message.author == client.user:
            return
        username: str = str(message.author)
        channel: str = str(message.channel)
        user_message: str = str(message.content)
        print(f"{username} said: '{user_message}' ({channel})")

        if user_message not in ['/help','/theguy','/thedad','/thepark','/lucky','/leave','/sunny','/theboys']: # add new show command here
            return
        if user_message[0] == '?':
            user_message: str = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
