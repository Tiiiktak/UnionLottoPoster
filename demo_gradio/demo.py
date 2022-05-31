import cv2
import gradio as gr
from lotto_poster.utils import CrawlerConfig, PosterDrawerConfig
from lotto_poster import get_lotto_crawler, PosterDrawer


def greet(date, lotto_cks):
    crawler = get_lotto_crawler(CrawlerConfig)
    ssq = crawler.get_latest_ssq_winning_info() if '双色球' in lotto_cks else None
    kl8 = crawler.get_latest_kl8_winning_info() if '快乐8' in lotto_cks else None
    fc3d = crawler.get_latest_fc3d_winning_info() if '福彩3D' in lotto_cks else None
    qlc = crawler.get_latest_qlc_winning_info() if '七乐彩' in lotto_cks else None

    drawer = PosterDrawer(PosterDrawerConfig)
    poster = drawer.draw(date, ssq=ssq, kl8=kl8, fc3d=fc3d, qlc=qlc)
    cv2.imwrite('poster.jpg', poster)
    return poster


demo = gr.Interface(fn=greet,
                    inputs=["text",
                            gr.CheckboxGroup(['双色球', '快乐8', '福彩3D', '七乐彩'],
                                             label='彩票种类'),
                            ], outputs="image")

demo.launch()
