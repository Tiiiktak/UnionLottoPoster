from lotto_poster.utils import CrawlerConfig, PosterDrawerConfig
from lotto_poster.crawler import get_lotto_crawler
from lotto_poster.drawer import PosterDrawer
from lotto_poster.app.static import StaticImageService
import time
import cv2


class PosterService:
    @classmethod
    def latest_poster(cls, date: str = 'today', ssq: bool = True, kl8: bool = True, qlc: bool = True, fc3d: bool = True):
        crawler = get_lotto_crawler(CrawlerConfig)
        drawer = PosterDrawer(PosterDrawerConfig)
        ssq_info = crawler.get_latest_ssq_winning_info() if ssq else None
        kl8_info = crawler.get_latest_kl8_winning_info() if kl8 else None
        qlc_info = crawler.get_latest_qlc_winning_info() if qlc else None
        fc3d_info = crawler.get_latest_fc3d_winning_info() if fc3d else None
        if date == 'today':
            date = time.strftime("%Y.%m.%d", time.localtime())  # 日期
        poster = drawer.draw(date=date, ssq=ssq_info, kl8=kl8_info, qlc=qlc_info, fc3d=fc3d_info)
        return poster

    @classmethod
    def poster_static(cls, img):
        img_name = StaticImageService.save_static_img(img)
        return img_name

    @classmethod
    def get_image(cls, img_name: str):
        img = StaticImageService.get_poster_by_name(img_name)
        return img

