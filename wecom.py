#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : main.py
# @Author: bjxing
# @Date  : 2024/01/02
# @Desc  : 企业微信

import requests
import json

from configparser import ConfigParser
from args_parser import get_config_file
from logger_config import setup_logger

logger = setup_logger()
config_file = get_config_file()
config = ConfigParser()
config.read(config_file, encoding='utf-8')


class WeCom(object):
    def __init__(self):
        self.logger = logger.debug
        self.url = "https://qyapi.weixin.qq.com"
        self.corpid = config.get('Wecom', 'corpid')
        self.secret = config.get('Wecom', 'secret')
        self.agentid = config.get('Wecom', 'agentid')
        self.touser = config.get('Wecom', 'touser')
        self.toparty = config.get('Wecom', 'toparty')
        self.msg = None
        self.token = None

    def access_token(self):
        url_arg = "/cgi-bin/gettoken?corpid={ID}&corpsecret={SECRET}".format(ID=self.corpid, SECRET=self.secret)
        url = self.url + url_arg
        response = requests.get(url)
        text = response.text
        self.token = json.loads(text)['access_token']
        self.logger(f"正在获取企业微信token：{self.token}")

    def send_messages(self, msg):
        self.access_token()
        values = {
            "touser": self.touser,
            "toparty": self.toparty,
            "msgtype": "text",
            "agentid": self.agentid,
            "text": {"content": msg},
            "safe": 0,
        }
        self.msg = values
        self.logger(f"发送企业微信内容：{self.msg}")
        send_url = '{url}/cgi-bin/message/send?access_token={token}'.format(url=self.url, token=self.token)
        response = requests.post(url=send_url, json=self.msg)
        self.logger(f"response状态：{response}")
