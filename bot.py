import discord
from discord.ext import commands

PREFIX = "ф!"
TOKEN = ""

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.command(name="хелп")
async def helper(ctx, member: discord.Member = None):
    await ctx.send(f"Префикс: ф!\nКоманды: обнять, пат, лизь, кусь, буп, поцеловать")

@bot.command(name="обнять")
async def hug(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send(f"{ctx.author.mention}, укажите кого обнять! Пример: `{PREFIX}обнять @user`")
        return
    if member == ctx.author:
        await ctx.send(f"{ctx.author.mention} обнял сам себя!")
        return
    if member == bot.user:
        await ctx.send(f"{ctx.author.mention} обнял меня! Спасибо, взаимно!")
        return
    await ctx.send(f"{ctx.author.mention} обнял {member.mention} :3")

@bot.command(name="пат")
async def pat(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send(f"{ctx.author.mention}, укажите кого погладить! Пример: `{PREFIX}пат @user`")
        return
    if member == ctx.author:
        await ctx.send(f"{ctx.author.mention} погладил сам себя!")
        return
    if member == bot.user:
        await ctx.send(f"{ctx.author.mention} погладил меня! Спасибо, взаимно! :3")
        return
    await ctx.send(f"{ctx.author.mention} погладил {member.mention} :3")

@bot.command(name="лизь")
async def pat(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send(f"{ctx.author.mention}, укажите кого лизнуть! Пример: `{PREFIX}лизь @user`")
        return
    if member == ctx.author:
        await ctx.send(f"{ctx.author.mention} лизнул сам себя!")
        return
    if member == bot.user:
        await ctx.send(f"{ctx.author.mention} лизнул меня! Спасибо, взаимно! :3")
        return
    await ctx.send(f"{ctx.author.mention} лизнул {member.mention} :3")

@bot.command(name="кусь")
async def pat(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send(f"{ctx.author.mention}, укажите кого кусьнуть! Пример: `{PREFIX}кусь @user`")
        return
    if member == ctx.author:
        await ctx.send(f"{ctx.author.mention} кусьнул сам себя!")
        return
    if member == bot.user:
        await ctx.send(f"{ctx.author.mention} кусьнул меня! ><")
        return
    await ctx.send(f"{ctx.author.mention} кусьнул {member.mention} >:3")

@bot.command(name="буп")
async def pat(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send(f"{ctx.author.mention}, укажите кого бупнуть! Пример: `{PREFIX}буп @user`")
        return
    if member == ctx.author:
        await ctx.send(f"{ctx.author.mention} бупнул сам себя!")
        return
    if member == bot.user:
        await ctx.send(f"{ctx.author.mention} бупнул меня! Спасибо, взаимно! :3")
        return
    await ctx.send(f"{ctx.author.mention} бупнул {member.mention} :3")

@bot.command(name="поцеловать")
async def hug(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send(f"{ctx.author.mention}, укажите кого поцеловать! Пример: `{PREFIX}поцеловать @user`")
        return
    if member == ctx.author:
        await ctx.send(f"{ctx.author.mention} поцеловал сам себя!")
        return
    if member == bot.user:
        await ctx.send(f"{ctx.author.mention} поцеловал меня! Спасибо, взаимно!")
        return
    await ctx.send(f"{ctx.author.mention} поцеловал {member.mention} :3")

def run_bot():
    try:
        bot.run(TOKEN)
    except:
        run_bot()

run_bot()