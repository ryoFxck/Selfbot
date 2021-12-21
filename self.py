import discord, os, random, sys, time, requests, json
from discord.ext import commands

# Config
config = {
    "token": "",
    "prefix": "$"
}

# Variables
token = config['token']
prefix = config['prefix']
client = discord.Client()
client = commands.Bot(command_prefix=prefix, self_bot=True)
url = 'https://discordapp.com/api/v6/users/@me'

# Colors
class colors:
    BLACK = '\33[30m'
    RED = '\33[31m'
    GREEN = '\33[32m'
    YELLOW = '\33[33m'
    BLUE = '\33[34m'
    VIOLET = '\33[35m'
    BEIGE = '\33[36m'
    WHITE = '\33[37m'


# Functions
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)


def Hex():
    hex = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return hex


def Main():
    prefix = config["prefix"]
    print(f'''{colors.RED}
▄███▄     ▄▄▄▄▀ ▄  █ ▄█   ▄   █▀▄▀█ 
█▀   ▀ ▀▀▀ █   █   █ ██    █  █ █ █ 
██▄▄       █   ██▀▀█ ██ █   █ █ ▄ █ 
█▄   ▄▀   █    █   █ ▐█ █   █ █   █ 
▀███▀    ▀        █   ▐ █▄ ▄█    █  
                 ▀       ▀▀▀    ▀   
    {colors.WHITE}Logged in: {colors.RED}{client.user.name}#{client.user.discriminator}
    {colors.WHITE}Prefix: {colors.RED}{prefix}              
    ''')


def Init():
    token = config["token"]
    try:
        client.run(token, bot=False)
    except discord.errors.LoginFailure:
        print(colors.RED + '[!]' + colors.WHITE +
              ' The token entered is not valid')

# Events 

@client.event
async def on_connect():
    cls()
    Main()


@client.command()
async def token(ctx, rtoken):
    await ctx.message.delete()
    data = {'Authorization': rtoken, 'Content-Type': 'application/json'}
    x = requests.get('https://discordapp.com/api/v6/users/@me', headers=data)

    if x.status_code != 200:
        await ctx.send('[!] The token you entered is invalid')
    else:
        x = x.json()
        username = x['username']
        id = x['id']
        discriminator = x['discriminator']
        nsfw = x['nsfw_allowed']
        email = x['email']
        phone = x['phone']
        mfa = x['mfa_enabled']
        verified = x['verified']
        InfoToken = discord.Embed(title=f'Token Info', color=Hex())
        InfoToken.add_field(name='Name', value=f'{username}#{discriminator}')
        await ctx.send(embed=InfoToken)

@client.command()
async def clear(ctx):
    await ctx.message.delete()
    async for message in ctx.message.channel.history.filter(lambda m: m.author == client.user).map(
                lambda m: m):
            try:
                await message.delete()
            except:
                pass

if __name__ == '__main__':
    Init()
