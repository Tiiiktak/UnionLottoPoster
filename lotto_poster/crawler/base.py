from typing import List, Any
import abc
from lotto_poster.utils import SSQWinningInfo, KL8WinningInfo, QLCWinningInfo, FC3DWinningInfo


class LottoCrawlerBase(abc.ABC):
    def __init__(self, config):
        self.config = config
        self.base_url = config.url
        header_config = config.header
        self.headers = {}
        for header_item in header_config.keys():
            if header_config[header_item]:
                self.headers[header_item] = header_config[header_item]

    @abc.abstractmethod
    def get_latest_ssq_winning_info(self) -> SSQWinningInfo:
        pass

    @abc.abstractmethod
    def get_latest_kl8_winning_info(self) -> KL8WinningInfo:
        pass

    @abc.abstractmethod
    def get_latest_fc3d_winning_info(self) -> FC3DWinningInfo:
        pass

    @abc.abstractmethod
    def get_latest_qlc_winning_info(self) -> QLCWinningInfo:
        pass

    @abc.abstractmethod
    def collect_recent_infos(self, stages: int = 30):
        pass
