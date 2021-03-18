from discord.ext import commands
# import asyncio
import random
# from datetime import datetime
MYID = 749127899981807686
TESTID = 713599800804638820


class Wadai(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print("wadai init")
        self.l_strip = [697723723016306712, 0]
        f = open("data/wadai.txt", "r", encoding="utf-8")
        self.datalist = f.readlines()
        print(len(self.datalist))

    def randomwadai(self, num):
        d = []
        for i in range(num):
            d.append(self.datalist[random.randint(0, len(self.datalist) - 1)])
        return(d)

    '''
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
        self.ahoset = set()
        for lines in self.bot.config.values():
            print(lines)
            self.wdch = lines.get("Wadaichannel")
            if (self.wdch is not None) and (self.wdch != 0):
                self.ahoset.add(self.wdch)
        print(self.ahoset)
         await self.wadaicheck(self.ahoset)
         await asyncio.sleep(300)
         await self.wadailoop()
    '''

    @commands.command()
    async def wadainow(self, ctx, *args):
        try:
            """zm.wadai [話題数(3)] 話題を今すぐ出す"""
            if args == ():
                num = 3
            else:
                num = int(args[0])
            d = self.randomwadai(num)
            text = ""
            i = 1
            for s in d:
                text += str(i) + ": " + s
                i += 1
            await ctx.send(text)
        except Exception as e:
            await self.bot.error(ctx, e)


def setup(bot):
    bot.add_cog(Wadai(bot))
