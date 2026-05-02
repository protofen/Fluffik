import discord
from discord.ext import commands
import random

PREFIX = "ф!"
TOKEN = ""

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

url = "https://raw.githubusercontent.com/protofen/Fluffik/refs/heads/main/img"
kiss_url = url + "/kiss/"
bite_url = url + "/bite/"
boop_url = url + "/boop/"
hug_url = url + "/hug/"
lick_url = url + "/lick/"
pat_url = url + "/pat/"
hug_item = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg']
kiss_item = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg']
lick_item = ['1.jpg']
pat_item = ['1.jpg']
bite_item = ['1.jpg']
boop_item = ['1.jpg']

@bot.command(name="хелп")
async def helper(ctx, member: discord.Member = None):
    await ctx.send(f"Префикс: ф!\nКоманды: обнять, пат, лизь, кусь, буп, поцеловать")

@bot.command(name="обнять")
async def hug(ctx, member: discord.Member = None):
    hug_sel = hug_url + random.choice(hug_item)
    if member is None:
        await ctx.send(f"{ctx.author.mention}, укажите кого обнять! Пример: `{PREFIX}обнять @user`")
        return
    if member == ctx.author:
        await ctx.send(f"{ctx.author.mention} обнял сам себя!")
        return
    if member == bot.user:
        await ctx.send(f"{ctx.author.mention} обнял меня! Спасибо, взаимно!")
        return
    await ctx.send(f"{ctx.author.mention} обнял {member.mention} :3\n{hug_sel}")

@bot.command(name="пат")
async def pat(ctx, member: discord.Member = None):
    pat_sel = pat_url + random.choice(pat_item)
    if member is None:
        await ctx.send(f"{ctx.author.mention}, укажите кого погладить! Пример: `{PREFIX}пат @user`")
        return
    if member == ctx.author:
        await ctx.send(f"{ctx.author.mention} погладил сам себя!")
        return
    if member == bot.user:
        await ctx.send(f"{ctx.author.mention} погладил меня! Спасибо, взаимно! :3")
        return
    await ctx.send(f"{ctx.author.mention} погладил {member.mention} :3\n{pat_sel}")

@bot.command(name="лизь")
async def pat(ctx, member: discord.Member = None):
    lick_sel = lick_url + random.choice(lick_item)
    if member is None:
        await ctx.send(f"{ctx.author.mention}, укажите кого лизнуть! Пример: `{PREFIX}лизь @user`")
        return
    if member == ctx.author:
        await ctx.send(f"{ctx.author.mention} лизнул сам себя!")
        return
    if member == bot.user:
        await ctx.send(f"{ctx.author.mention} лизнул меня! Спасибо, взаимно! :3")
        return
    await ctx.send(f"{ctx.author.mention} лизнул {member.mention} :3\n{lick_sel}")

@bot.command(name="кусь")
async def pat(ctx, member: discord.Member = None):
    bite_sel = bite_url + random.choice(bite_item)
    if member is None:
        await ctx.send(f"{ctx.author.mention}, укажите кого кусьнуть! Пример: `{PREFIX}кусь @user`")
        return
    if member == ctx.author:
        await ctx.send(f"{ctx.author.mention} кусьнул сам себя!")
        return
    if member == bot.user:
        await ctx.send(f"{ctx.author.mention} кусьнул меня! ><")
        return
    await ctx.send(f"{ctx.author.mention} кусьнул {member.mention} >:3\n{bite_sel}")

@bot.command(name="буп")
async def pat(ctx, member: discord.Member = None):
    boop_sel = boop_url + random.choice(boop_item)
    if member is None:
        await ctx.send(f"{ctx.author.mention}, укажите кого бупнуть! Пример: `{PREFIX}буп @user`")
        return
    if member == ctx.author:
        await ctx.send(f"{ctx.author.mention} бупнул сам себя!")
        return
    if member == bot.user:
        await ctx.send(f"{ctx.author.mention} бупнул меня! Спасибо, взаимно! :3")
        return
    await ctx.send(f"{ctx.author.mention} бупнул {member.mention} :3\n{boop_sel}")

@bot.command(name="поцеловать")
async def hug(ctx, member: discord.Member = None):
    kiss_sel = kiss_url + random.choice(kiss_item)
    if member is None:
        await ctx.send(f"{ctx.author.mention}, укажите кого поцеловать! Пример: `{PREFIX}поцеловать @user`")
        return
    if member == ctx.author:
        await ctx.send(f"{ctx.author.mention} поцеловал сам себя!")
        return
    if member == bot.user:
        await ctx.send(f"{ctx.author.mention} поцеловал меня! Спасибо, взаимно!")
        return
    await ctx.send(f"{ctx.author.mention} поцеловал {member.mention} :3\n{kiss_sel}")

def run_bot():
    try:
        bot.run(TOKEN)
    except:
        run_bot()

run_bot()