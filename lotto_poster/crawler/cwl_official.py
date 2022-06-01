from .base import LottoCrawlerBase
from lotto_poster.utils import CrawlerException, SSQWinningInfo, KL8WinningInfo, FC3DWinningInfo, QLCWinningInfo
from random import randint
from typing import Optional, List, Union, Any
import requests
import json


class CWLOfficialCrawler(LottoCrawlerBase):
    def __init__(self, config):
        super().__init__(config)

    def get_latest_ssq_winning_info(self) -> SSQWinningInfo:
        ssq_url = f'{self.base_url}?name=ssq&issueCount=1'
        result = self.__get_url_winning_infos(ssq_url)[0]
        return self.__format_info(result, "ssq")

    def get_latest_kl8_winning_info(self) -> KL8WinningInfo:
        kl8_url = f'{self.base_url}?name=kl8&issueCount=1'
        result = self.__get_url_winning_infos(kl8_url)[0]
        return self.__format_info(result, "kl8")

    def get_latest_fc3d_winning_info(self) -> FC3DWinningInfo:
        fc3d_url = f'{self.base_url}?name=3d&issueCount=1'
        result = self.__get_url_winning_infos(fc3d_url)[0]
        return self.__format_info(result, "fc3d")

    def get_latest_qlc_winning_info(self) -> QLCWinningInfo:
        qlc_url = f'{self.base_url}?name=qlc&issueCount=1'
        result = self.__get_url_winning_infos(qlc_url)[0]
        return self.__format_info(result, "qlc")

    def collect_recent_infos(self, stages: int = 30,
                             lotto_type: List[str] = ('ssq', 'kl8', 'fc3d', 'qlc')) -> List[Any]:
        results = []
        for t in lotto_type:
            name = t if t != 'fc3d' else '3d'
            target_url = f'{self.base_url}?name={name}&issueCount={stages}'
            winning_infos = self.__get_url_winning_infos(target_url)
            for w_info in winning_infos:
                results.append(self.__format_info(w_info, t))
        return results

    def __get_url_winning_infos(self, url: str) -> dict:
        try:
            header = self.headers.copy()
            header['Cookie'] = header['Cookie'][:-1] + str(randint(1, 100))
            requests.adapters.DEFAULT_RETRIES = 5  # 增加重连次数
            s = requests.session()
            s.keep_alive = False
            result = s.get(url, headers=header).json()
            # result = requests.get(url, headers=Headers).json()
        except json.decoder.JSONDecodeError:
            raise CrawlerException('访问频繁，数据爬取失败，稍后再试', 400)
        if result['state'] != 0:
            raise CrawlerException(result['message'], 400)
        return result['result']

    def __format_info(self, winning_dict, name: str) -> Union[SSQWinningInfo, KL8WinningInfo,
                                                              FC3DWinningInfo, QLCWinningInfo]:
        if winning_dict['poolmoney'] == "_":
            winning_dict['poolmoney'] = 0
        if name == 'ssq':
            red_balls = list(map(int, winning_dict['red'].split(',')))
            blue_ball = int(winning_dict['blue']) if isinstance(winning_dict['blue'], str) else winning_dict['blue']
            return SSQWinningInfo(
                stage=winning_dict['code'],
                date=winning_dict['date'].split('(')[0],
                week=winning_dict['week'],
                red_code=red_balls,
                blue_code=blue_ball,
                pool_money=winning_dict['poolmoney'],
                first_prize_content=winning_dict['content'],
                prize_grades=winning_dict['prizegrades'])
        elif name == 'kl8':
            red_balls = list(map(int, winning_dict['red'].split(',')))
            return KL8WinningInfo(
                stage=winning_dict['code'],
                date=winning_dict['date'].split('(')[0],
                week=winning_dict['week'],
                red_code=red_balls,
                pool_money=winning_dict['poolmoney'],
                first_prize_content=winning_dict['content'],
                prize_grades=winning_dict['prizegrades'])
        elif name == 'fc3d':
            red_balls = list(map(int, winning_dict['red'].split(',')))
            return FC3DWinningInfo(
                stage=winning_dict['code'],
                date=winning_dict['date'].split('(')[0],
                week=winning_dict['week'],
                red_code=red_balls)
        elif name == 'qlc':
            red_balls = list(map(int, winning_dict['red'].split(',')))
            blue_ball = int(winning_dict['blue']) if isinstance(winning_dict['blue'], str) else winning_dict['blue']
            return QLCWinningInfo(
                stage=winning_dict['code'],
                date=winning_dict['date'].split('(')[0],
                week=winning_dict['week'],
                red_code=red_balls,
                blue_code=blue_ball,
                pool_money=winning_dict['poolmoney'],
                first_prize_content=winning_dict['content'],
                prize_grades=winning_dict['prizegrades'])
        else:
            raise CrawlerException('未知彩种')
