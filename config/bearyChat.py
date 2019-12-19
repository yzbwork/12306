# -*- coding: utf8 -*-
import requests
import json
import TickerConfig


def notification_by_bearyChat():

    webHookUrl = TickerConfig.BEARY_CHART_CONF["url"]
    is_enable = TickerConfig.BEARY_CHART_CONF["is_enable"]
    if ( is_enable and webHookUrl.strip() != ""):
        try:
            params = {
              "text": "购票成功"
            }
            headers = {'Content-Type': 'application/json'}
            bearyChatResponse = requests.post(webHookUrl, data=json.dumps(params), headers=headers)
            bearyChatResponse.encoding = "utf-8"
            print(bearyChatResponse.text)
        except Exception as e:
            print(u"倍洽 配置有误 {}".format(e))
    else:
        print(u"倍洽通知 未执行")


if __name__ == "__main__":
    notification_by_bearyChat()
