import discord
import traceback
from discord.ext import commands
from os import getenv

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
 
client.on('messegeCreate',message => {
  if (message.author.bot) return;
    if (message.guild.id !== "1086670878084956300")
      if (message.cotent.match(/[0-9][0-9][0-9][0-9][0-9]/))
        if(message.cotent.match(/[^0-9]/)) return;
        if(message.content.match(/[0-9][0-9][0-9][0-9][0-9][0-9]/)) return;
     client.channels.cache.get('1086678028396003328').send(`${message.content}`)
   }
});



client.on('messageCreate' ,message => {
  if(message.guild.id !== "1086678028396003328")
  return;
    if(message.channel.id !=== '1086644609016397848'){
  message.channel.setName("vc〖" + `${message.content}` + "〗")
  return;
  }
});

token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)

