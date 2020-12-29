from discord.ext import commands
import asyncio
from datetime import datetime, timedelta, timezone
MYID = 749127899981807686
TESTID = 713599800804638820


class Wadai(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        print("wadai init")
        self.l_strip = [697723723016306712, 0]

    def randomwadai(self):
        return "ばーか"

    async def wadaicheck(self, args):
        global MYID, TESTID
        for id in args:
            if id is not None:
                print(id)
                channel = self.bot.get_channel(id)
                if channel is None:
                    continue
                hst = await channel.history(limit=1).flatten()
                if hst[0].author.id != MYID and hst[0].author.id != TESTID:
                    print(hst[0].created_at)
                    if (datetime.utcnow() - hst[0].created_at).total_seconds() >= 7200:
                        await channel.send(self.randomwadai())
                        break

    async def wadailoop(self):
        await self.wadaicheck(self.l_strip)
        await asyncio.sleep(300)
        await self.wadailoop()

    @commands.command()
    async def wadainow(self, ctx):
        await ctx.send(self.randomwadai())


def setup(bot):
    bot.add_cog(Wadai(bot))
