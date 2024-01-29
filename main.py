#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : main.py
# @Author: bjxing
# @Date  : 2024/01/05
# @Desc  : 主代码

import datetime
import time
from configparser import ConfigParser
from args_parser import get_config_file
from logger_config import setup_logger
from wecom import WeCom

logger = setup_logger()
config_file = get_config_file()
config = ConfigParser()
cfg = config.read(config_file, encoding='utf-8')


def get_duty_person(section, day):
    set_date = config.get(section, 'set_data')
    personnel = config.get(section, 'personnel').split(',')
    curr_date = str(datetime.date.today() + datetime.timedelta(days=+day))
    str_set_date = datetime.datetime.strptime(set_date, '%Y-%m-%d').date()
    str_curr_date = datetime.datetime.strptime(curr_date, '%Y-%m-%d').date()
    diff_date = str_curr_date - str_set_date
    curr_person = personnel[diff_date.days % len(personnel)]
    return curr_person


if __name__ == "__main__":
    try:
        current_date = str(datetime.date.today())
        hour = time.localtime().tm_hour
        for section in config.sections():
            if section.startswith('Person'):
                if hour < 20:
                    data = """尊敬的【{}】运维值班人员【{}】:
                您好！根据公司安排，您将于今日【{}】在【{}】进行值班工作。请您务必准时到岗，认真履行职责，确保公司信息系统的稳定运行。""" \
                        .format(config.get(section, 'team'), str(get_duty_person(section, 0)), str(current_date),
                                config.get(section, 'duty_period'))
                else:
                    data = """叮~您好！明天您【{}】有值班任务，请准时到岗，确保公司信息系统的稳定运行。""" \
                        .format(str(get_duty_person(section, 1)))
                wechat = WeCom()
                wechat.send_messages(data)
    except Exception as e:
        logger.exception("发送出现异常：%s", str(e))
