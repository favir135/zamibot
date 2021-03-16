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

            d_day = datetime.datetime.now(datetime.timezone(
                datetime.timedelta(hours=9))) + datetime.timedelta(days=-1)
            dt = datetime.datetime(
                d_day.year, d_day.month, d_day.day, 15, 0, 0, 0)
            print(dt)
            fucktime = dt - datetime.timedelta(days=7)
            print(fucktime)
            idset = set()
            hst = await ctx.history(before=dt, after=fucktime, limit=10000).flatten()
            print(str(len(hst)))
            for message in hst:
                auth = message.author
                if (not auth.bot) and (not auth.system):
                    counter += 1
                    idset.add(auth.id)
            await ctx.send('done!')
            # print(idset)
        await ctx.send("過去7日間の会話数は" + str(counter) + "\n1日平均は" + str(math.floor(counter / 7 * 100) / 100) + "\n過去７日間のアクティブユーザー数は" + str(len(idset)))


def setup(bot):
    bot.add_cog(Stats(bot))
