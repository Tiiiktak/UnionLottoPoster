import os.path as osp
import cv2
import numpy as np
from lotto_poster.utils import SSQWinningInfo, KL8WinningInfo, QLCWinningInfo, FC3DWinningInfo


class PosterDrawer:
    def __init__(self, config):
        self.config = config
        self.border_width = config.border_width
        self.border_color = config.border_color
        self.img_directory = config.background_img.absolute_path
        self.bg_top_cfg = config.background_img.top
        self.bg_bottom_cfg = config.background_img.bottom
        self.bg_ssq_cfg = config.background_img.ssq
        self.bg_fc3d_cfg = config.background_img.fc3d
        self.bg_kl8_cfg = config.background_img.kl8
        self.bg_qlc_cfg = config.background_img.qlc

    def draw(self, date: str,
             ssq: SSQWinningInfo = None,
             fc3d: FC3DWinningInfo = None,
             kl8: KL8WinningInfo = None,
             qlc: QLCWinningInfo = None):
        img_stack = [self.draw_top_subimg(date), ]
        if ssq is not None:
            img_stack.append(self.draw_ssq_subimg(ssq))
        if fc3d is not None:
            img_stack.append(self.draw_fc3d_subimg(fc3d))
        if kl8 is not None:
            img_stack.append(self.draw_kl8_subimg(kl8))
        if qlc is not None:
            img_stack.append(self.draw_qlc_subimg(qlc))
        img_stack.append(self.draw_bottom_subimg())
        poster = concat_subimgs(img_stack)
        poster = self.draw_poster_border(poster)
        return poster

    def draw_top_subimg(self, date: str):
        """
        生成顶部子图（标题，含日期）
        :param date: 2022.06.01 like
        """
        img_path = osp.join(self.img_directory, self.bg_top_cfg.img)
        img = cv2.imread(img_path)

        img = cv2.putText(img, date, self.bg_top_cfg.date_position,
                          cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 3, (0, 0, 0), 10)
        return img

    def draw_bottom_subimg(self):
        img_path = osp.join(self.img_directory, self.bg_bottom_cfg.img)
        img = cv2.imread(img_path)
        return img

    def draw_ssq_subimg(self, ssq_info: SSQWinningInfo):
        img_path = osp.join(self.img_directory, self.bg_ssq_cfg.img)
        img = cv2.imread(img_path)

        stage_text = ssq_info.stage
        balls = ssq_info.red_code + [ssq_info.blue_code]
        img = cv2.putText(img, stage_text, self.bg_ssq_cfg.stage_position,
                          cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2.2, (0, 0, 0), 5)

        code_x, code_y = self.bg_ssq_cfg.code_position[:2]
        code_inter = self.bg_ssq_cfg.code_position[2]
        for idx, ball in enumerate(balls):
            ball_text = str(ball).rjust(2, '0')
            img = cv2.putText(img, ball_text,
                              (code_x + idx * code_inter, code_y),
                              cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2.8, (255, 255, 255), 7)
        return img

    def draw_fc3d_subimg(self, fc3d_info: FC3DWinningInfo):
        img_path = osp.join(self.img_directory, self.bg_fc3d_cfg.img)
        img = cv2.imread(img_path)

        stage_text = fc3d_info.stage
        img = cv2.putText(img, stage_text, self.bg_fc3d_cfg.stage_position,
                          cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2.2, (0, 0, 0), 5)

        code_x, code_y = self.bg_fc3d_cfg.code_position[:2]
        code_inter = self.bg_fc3d_cfg.code_position[2]
        for idx, ball in enumerate(fc3d_info.red_code):
            ball_text = str(ball)
            img = cv2.putText(img, ball_text,
                              (code_x + idx * code_inter, code_y),
                              cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2.8, (255, 255, 255), 7)
        return img

    def draw_kl8_subimg(self, kl8_info: KL8WinningInfo):
        img_path = osp.join(self.img_directory, self.bg_kl8_cfg.img)
        img = cv2.imread(img_path)

        stage_text = kl8_info.stage
        img = cv2.putText(img, stage_text, self.bg_kl8_cfg.stage_position,
                          cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2.2, (0, 0, 0), 5)

        code_x, code_y = self.bg_kl8_cfg.code_position[:2]
        code_inter_x, code_inter_y = self.bg_kl8_cfg.code_position[2:]
        for idx, ball in enumerate(kl8_info.red_code):
            ball_text = str(ball).rjust(2, '0')
            x_idx = idx % 5
            y_idx = idx // 5
            img = cv2.putText(img, ball_text,
                              (code_x + x_idx * code_inter_x, code_y + y_idx * code_inter_y),
                              cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2.8, (255, 255, 255), 7)
        return img

    def draw_qlc_subimg(self, qlc_info: QLCWinningInfo):
        img_path = osp.join(self.img_directory, self.bg_qlc_cfg.img)
        img = cv2.imread(img_path)

        stage_text = qlc_info.stage
        img = cv2.putText(img, stage_text, self.bg_qlc_cfg.stage_position,
                          cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2.2, (0, 0, 0), 5)

        code_x, code_y = self.bg_qlc_cfg.red_code_position[:2]
        code_inter = self.bg_qlc_cfg.red_code_position[2]
        for idx, ball in enumerate(qlc_info.red_code):
            ball_text = str(ball).rjust(2, '0')
            img = cv2.putText(img, ball_text,
                              (code_x + idx * code_inter, code_y),
                              cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2.8, (255, 255, 255), 7)

        blue_text = str(qlc_info.blue_code).rjust(2, '0')
        img = cv2.putText(img, blue_text, self.bg_qlc_cfg.blue_code_position,
                          cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2.8, (255, 255, 255), 7)
        return img

    def draw_poster_border(self, poster):
        bw = self.border_width
        border_color = self.border_color[::-1]
        poster = cv2.copyMakeBorder(poster, bw, bw, bw, bw, cv2.BORDER_CONSTANT,
                                    value=border_color)
        return poster


def concat_subimgs(img_stack: list):
    if len(img_stack) == 0:
        return None
    img_stack = tuple(img_stack)
    img = np.vstack(img_stack)
    return img
