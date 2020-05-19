#!/usr/bin/env python
# coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
import json


def send_sms(template, phone):
    client = AcsClient('LTAI4FcjABKaRgi17wQL3P1K', 'Mp2bgtYDAhGqndWMeIpdTW6BOauART', 'default')
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('http')  # https | http
    request.set_version('2017-05-25')

    # set_action_name 这个是选择你调用的接口的名称，如：SendSms，SendBatchSms等
    request.set_action_name('SendSms')
    # request.set_action_name('QuerySendDetails')

    # 这个参数也是固定的
    request.add_query_param('RegionId', "default")  # 98A66994-3DF4-4FA5-A33F-CCB36EB599D0
    # request.add_query_param('RegionId', "cn-hangzhou")

    request.add_query_param('PhoneNumbers', phone)  # 发给谁
    request.add_query_param('SignName', "飞箭加速")  # 签名
    request.add_query_param('TemplateCode', "SMS_188055127")  # 模板编号
    request.add_query_param('TemplateParam', f"{template}")  # 发送验证码内容
    response = client.do_action_with_exception(request)

    return response

    # response = client.do_action(request)
    # # python2:  print(response)
    # print(str(response, encoding='utf-8'))


if __name__ == '__main__':
    template = {
        'code': '556634',
    }
    res = send_sms(template, phone=13640665084)
    print(str(res, encoding='utf-8'))
    res_dict = json.loads(res)
    print(res_dict)
    if res_dict.get('Message') == 'OK' and res_dict.get('Code') == 'OK':
        print("成功啦")
    else:
        print("失败啦")
