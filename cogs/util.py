from discord.ext import commands
import datetime
import math
import time


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("stats init")

    @commands.command()
    async def stats(self, ctx):
        """過去7日間の会話数を表示"""
        try:
            basetime = time.time()
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
                hst = [message async for message in ctx.history(before=dt, after=fucktime, limit=10000) if not (message.author.bot or message.author.system)]
                print(str(len(hst)))
                counter2 = 0
                for message in hst:
                    if not (message.author.bot or message.author.system):
                        counter2 += 1
                    idset.add(message.author.id)

                counter = len(hst)
                print(counter2)
            elapsed = math.floor((time.time() - basetime) * 100) / 100
            print(elapsed)
            await ctx.send("過去7日間の会話数は" + str(counter) + "\n1日平均は" + str(math.floor(counter / 7 * 100) / 100) + "\n過去７日間のアクティブユーザー数は" + str(len(idset)) + "\n`" + str(elapsed) + " 秒で実行`")
        except Exception as e:
            await self.bot.error(ctx, e)


def setup(bot):
    bot.add_cog(Utility(bot))
