import configparser
from discord.ext import commands
# import dotenv
import os

# 自分のBotのアクセストークンに置き換えてくださ
path = "config.ini"
# dotenv_path = ".env"

l_strip = []
MYID = 749127899981807686
TESTID = 713599800804638820

# 接続に必要なオブジェクトを生成

bot = commands.Bot(command_prefix='zm.')

'''
設定
1 サーバーid , 話題提供チャンネルのid ,
'''

bot.config = configparser.ConfigParser()
bot.config.read(path, encoding='utf-8')
print(bot.config.sections())

# dotenv.load_dotenv(dotenv_path)
TOKEN = os.environ.get("ZAMIBOT_TOKEN")
# print(TOKEN)
# def parsetopic(channel):


# 起動時に動作する処理
@bot.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
    bot.load_extension('cogs.greet')
    bot.load_extension('cogs.wadai')
    bot.load_extension('cogs.stats')
    wadai = bot.get_cog('Wadai')
    # await wadai.wadailoop()


# メッセージ受信時に動作する処理
@bot.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')

    await bot.process_commands(message)


@bot.command()
async def test(ctx, arg):
    print("fuck")
    await ctx.send(arg)

'''
@bot.command()
async def add(ctx):
    print("aa")
    print(l_strip)
    try:
        if(ctx.channel.id in l_strip):
            await ctx.send("すでに登録されています。^^;")
            return
        else:
            writesettings(ctx.channel.id)

    except Exception as e:
        await ctx.send("エラー\n```" + str(e) + "```")
    else:
        await ctx.send("登録完了しました")
'''

# Botの起動とDiscordサーバーへの接続
bot.run(TOKEN)
