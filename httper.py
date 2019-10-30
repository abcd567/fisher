# _*_ coding: utf-8 _*_
__author__ = "吴飞鸿"
__date__ = "2019/10/30 23:25"

import requests

class HTTP:
    @staticmethod
    def get(url, return_json=True):
        res = requests.get(url)
        if res.status_code != 200:
            return {} if return_json else ''
        return res.json() if return_json else res.text