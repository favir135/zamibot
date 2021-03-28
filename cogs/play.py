from discord.ext import commands
import math


class Playings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        print("play init")

    @commands.command()
    async def spamcopy(self, ctx, *args):
        """スパム用に文字列をコピーしてDMに送る。なんて害悪なんだ！
        zm.spamcopy [コピーする文字列]
        -e everyoneメンション付き
        -n 1回ずつ改行
        -l [文字数] 最大文字数(デフォルト:1994)を指定
        """
        try:
            cpstr = args[0]
            everyone = False
            # newline = False
            limit = 1994
            i = 0
            for line in args:
                if line == "-e":
                    everyone = True
                elif line == "-n":
                    # newline = True
                    cpstr += "\n"
                elif line == "-l":
                    limit = int(args[i + 1])
                i += 1
            length = len(cpstr)
            print(str(int(limit / length)))
            if everyone:
                limit -= 10
                await ctx.author.send("```" + self.duplicate(cpstr, int(limit / length)) + " @everyone```")
            else:
                await ctx.author.send("```" + self.duplicate(cpstr, int(limit / length)) + "```")
        except Exception as e:
            await self.bot.error(ctx, e)

    @commands.command()
    async def heron(self, ctx, a: float, b: float, c: float):
        """三角形の面積を3辺の長さから求める
            zm.heron [辺1] [辺2] [辺3]
        """
        try:
            s = (a + b + c) / 2
            await ctx.send(math.sqrt(s * (s - a) * (s - b) * (s - c)))
        except Exception as e:
            await self.bot.error(e)

    def duplicate(self, s, time):
        tmp = ""
        for i in range(time):
            tmp += s
        return tmp


def setup(bot):
    bot.add_cog(Playings(bot))
