import uuid
import os
import time
import os.path as osp
import cv2
from apscheduler.schedulers.background import BackgroundScheduler


def check_static_dir(path, interval_seconds=300):
    if not osp.exists(path):
        return
    for file_name in os.listdir(path):
        if not file_name.endswith(".jpg"):
            continue
        create_time_stamp = file_name.split("_")[0]
        time_interval = time.time() - float(create_time_stamp)
        if time_interval > interval_seconds:
            os.remove(osp.join(path, file_name))


class StaticImageService:
    @classmethod
    def start_scheduler(cls):
        img_dir = osp.join('.', 'images')
        if not osp.exists(img_dir):
            os.mkdir(img_dir)
        scheduler = BackgroundScheduler()
        scheduler.add_job(check_static_dir,
                          'interval',
                          seconds=30,
                          args=[img_dir, 20])
        scheduler.start()

    @classmethod
    def save_static_img(cls, img):
        time_stamp = str(time.time()).split('.')[0]
        random_name = f'{time_stamp}_{str(uuid.uuid4())[:6]}.jpg'
        img_path = osp.join('./images', random_name)
        cv2.imwrite(img_path, img)
        return random_name

    @classmethod
    def get_poster_by_name(cls, img_name):
        img_path = osp.join('./images', img_name)
        if not osp.exists(img_path):
            raise FileExistsError(f'{img_name} not exists')
        img = cv2.imread(img_path)
        return img

