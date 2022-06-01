from lotto_poster.crawler import get_lotto_crawler
from lotto_poster.utils import CrawlerConfig, SSQWinningInfo, KL8WinningInfo, QLCWinningInfo, FC3DWinningInfo
from typing import Union, List, Any
from .dto import WinningInfoDto


class CrawlerService:
    @classmethod
    def get_winning_info(cls, lotto_type: str, stages: int) -> List[Any]:
        crawler = get_lotto_crawler(CrawlerConfig)
        if lotto_type not in ['ssq', 'kl8', 'fc3d', 'qlc']:
            raise ValueError('lotto_type must be one of ssq, kl8, fc3d, qlc')

        ans = crawler.collect_recent_infos(stages, lotto_type=[lotto_type])
        return ans

    @classmethod
    def format_winning_info(cls, info: Union[SSQWinningInfo, KL8WinningInfo,
                                             QLCWinningInfo, FC3DWinningInfo]) -> WinningInfoDto:
        tmp = WinningInfoDto(
            date=info.date,
            stage=info.stage,
            lotto_name=info.name,
            code=[],
        )
        if isinstance(info, SSQWinningInfo):
            tmp.code = info.red_code + [info.blue_code]
        elif isinstance(info, KL8WinningInfo):
            tmp.code = info.red_code
        elif isinstance(info, QLCWinningInfo):
            tmp.code = info.red_code + [info.blue_code]
        elif isinstance(info, FC3DWinningInfo):
            tmp.code = info.red_code
        else:
            raise ValueError('lotto_type must be one of ssq, kl8, fc3d, qlc')
        return tmp



