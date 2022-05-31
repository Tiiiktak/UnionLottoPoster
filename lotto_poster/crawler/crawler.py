from .cwl_official import CWLOfficialCrawler
from .base import LottoCrawlerBase
from lotto_poster.utils import CrawlerException


def get_lotto_crawler(config) -> LottoCrawlerBase:
    if config.web_type == 'cwl_official':
        return CWLOfficialCrawler(config)
    else:
        raise CrawlerException('Unknown web type: {}'.format(config.web_type))
