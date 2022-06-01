import yaml
import os
import os.path as osp
from munch import DefaultMunch


def get_config_dict(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        dict_data = yaml.load(f.read(), Loader=yaml.FullLoader)
    return dict_data


current_file_path = osp.abspath(osp.dirname(__file__))
config_path = os.path.abspath(os.path.join(current_file_path, '..', '..', 'config.yml'))

print('Loading config from: {}'.format(config_path))

config_dict = get_config_dict(config_path)

print('Config loaded: {}'.format(config_dict))

config = DefaultMunch.fromDict(config_dict)

AppConfig = config.app

CrawlerConfig = config.crawler

PosterDrawerConfig = config.poster_drawer


