#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Created by box on 2018/2/27.
import base64

from zhihu.utils import zhihu_utils

CONFIGS = zhihu_utils.get_configs()

URL_HOME_REQUEST = CONFIGS['URL']['HOME_REQUEST_URL']
URL_INDEX_REQUEST = CONFIGS['URL']['INDEX_REQUEST_URL']
URL_LOGIN_REQUEST = CONFIGS['URL']['LOGIN_REQUEST_URL']
URL_BATCH_REQUEST = CONFIGS['URL']['BATCH_REQUEST_URL']
URL_CAPTCHA_REQUEST = CONFIGS['URL']['CAPTCHA_REQUEST_URL']
URL_TOPSTORY_REQUEST = CONFIGS['URL']['TOPSTORY_REQUEST_URL']
URL_FIND_REQUEST = CONFIGS['URL']['FIND_REQUEST_URL']
URL_TOPIC_REQUEST = CONFIGS['URL']['TOPIC_REQUEST_URL']
URL_SHARETEXT_REQUEST = CONFIGS['URL']['SHARETEXT_REQUEST_URL']
URL_FOLLOWING_QUESTION_COUNT = CONFIGS['URL']['URL_FOLLOWING_QUESTION_COUNT']
URL_SWITCHS = CONFIGS['URL']['URL_SWITCHS']
URL_SUPPORTED_COUNTRISE = CONFIGS['URL']['URL_SUPPORTED_COUNTRISE']

# 这是固定的
AUTHORIZATION = CONFIGS['AUTH']['AUTHORIZATION']

HEADERS = CONFIGS['HEADERS']

CAPTCHA = {
    'img_size': [200, 44],
    'input_points': [],
}
CAPTCHA_POINTS = [[88, 12.6875], [112, 12.6875], [133, 15.6875], [159, 9.6875], [181, 18.6875],
                  [210, 16.6875], [236, 16.6875]]

CRAWL_DELAY = 2
