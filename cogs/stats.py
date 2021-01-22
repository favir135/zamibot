from discord.ext import commands
import datetime
import math


class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("stats init")

    @commands.command()
    async def stats(self, ctx):
        """
        過去7日間の会話数を表示
        """
        counter = 0
        async with ctx.typing():

            d_day = datetime.date.today() + datetime.timedelta(days=-1)
            dt = datetime.datetime(
                d_day.year, d_day.month, d_day.day, 15, 0, 0, 0)
            print(d_day)
            idset = set()
            async for message in ctx.history(before=dt, after=dt + datetime.timedelta(days=-7)):
                if (not message.author.bot) and (not message.author.system):
                    counter += 1
                    idset.add(message.author.id)
            await ctx.send('done!')
        await ctx.send("過去7日間の会話数は" + str(counter) + "\n1日平均は" + str(math.floor(counter / 7 * 100) / 100) + "\n過去７日間のアクティブユーザー数は" + str(len(idset)))


def setup(bot):
    bot.add_cog(Stats(bot))
