import discord
from discord.ext.commands import Bot, CommandNotFound
from discord.utils import get

bot = Bot(command_prefix='!')
bot.remove_command('help') 

def getToken():
	tokenFile = open('TOKEN.txt','r')
	tokentxt = tokenFile.read()
	return tokentxt

@bot.event
async def on_ready():
	print('logged in as '+str(bot.user))

@bot.command(name = "help")
async def help(ctx):
	await ctx.channel.send('''
Command prefix: !

Command: 

join-batch `batchname`

Eg: join-batch `batch-1`

leave-batch `batchname`

''')

@bot.command(name = 'join-batch')
async def join_batch(ctx, *args):

	user = ctx.message.author

	if not args:
		await ctx.channel.send("Try entering a batch for a role")
	
	elif len(args) != 1:
		await ctx.channel.send("Please enter only one batch")
	
	elif args[0] != "batch-1" and args[0] != "batch-2":
		await ctx.channel.send("Enter a valid batch")

	elif 'batch-1' in [y.name for y in user.roles] or 'batch-2' in [y.name for y in user.roles]:
		await ctx.channel.send("Sorry, can't have 2 batches at the same time. Leave batch and assign again")
	
	else:
		
		req_role = args[0]

		try:
			role = discord.utils.get(ctx.guild.roles, name = req_role)
			await user.add_roles(role)
			await ctx.channel.send("Added Role {} to {}".format(role.name, user.mention))
		
		except :
			await ctx.channel.send("Looks like the role {} isn't on this server.".format(req_role))


@bot.command(name = 'leave-batch')
async def leave_batch(ctx):

	user = ctx.message.author

	remove_role = None

	for role in user.roles:
		if 'batch' in role.name:
			remove_role = role
			break

	if remove_role:
		await user.remove_roles(remove_role)
		await ctx.channel.send("Removed {} from {}".format(user.mention, remove_role))
	
	else:
		await ctx.channel.send("Can't remove you since you haven't joined any batch")


@bot.event
async def on_command_error(self, ctx, error):
	if isinstance(error, CommandNotFound):
		await ctx.channel.send("Sorry {} ! Unknown command\nTry `!help` to see what I can do.".format(ctx.message.author.mention))

bot.run(getToken())