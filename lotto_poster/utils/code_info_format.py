
class BaseWinningInfo:
    name: str       # 彩种名称
    stage: str      # 期数
    date: str       # 开奖日期
    week: str       # 开奖日是周几
    red_code: list  # 红球
    blue_code: int  # 蓝球
    pool_money: float     # 奖池金额
    first_prize_content: str    # 一等奖各省中奖信息
    prize_grades: list          # 奖等列表

    def __init__(self, stage, red_code, date=None, week=None, pool_money=None,
                 first_prize_content=None, prize_grades=None, blue_code=None):
        self.stage = stage
        self.date = date
        self.week = week
        self.red_code = red_code
        self.pool_money = eval(pool_money) if pool_money else None
        self.first_prize_content = first_prize_content
        self.prize_grades = prize_grades
        self.blue_code = blue_code

    def print(self):
        print('彩种名称:', self.name)
        print('彩期:', self.stage)
        print(f'开奖日期: {self.date}(周{self.week})')
        print(f'开奖号: {self.red_code}' + (f' + {self.blue_code}' if self.blue_code else ''))
        print(f'奖池金额: {self.pool_money}元') if self.pool_money else None
        print(f'一等奖中奖信息: {self.first_prize_content}') if self.first_prize_content else None
        print(f'奖等: {self.prize_grades}') if self.prize_grades else None


class SSQWinningInfo(BaseWinningInfo):
    name = '双色球'


class KL8WinningInfo(BaseWinningInfo):
    name = '快乐8'


class FC3DWinningInfo(BaseWinningInfo):
    name = '福彩3D'


class QLCWinningInfo(BaseWinningInfo):
    name = '七乐彩'
