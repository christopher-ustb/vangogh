import hashlib
from urllib import parse

import requests

from vangogh import settings

_BAIDU_MAP_DOMAIN = "http://api.map.baidu.com"


def _generate_sn(uri):
    # 对queryStr进行转码，safe内的保留字符不转换
    encoded_str = parse.quote(uri, safe="/:=&?#+!$,;'@()*[]")
    # 在最后直接追加上yoursk
    raw_str = encoded_str + settings.BAIDU_MAP_SK
    sn = hashlib.md5(parse.quote_plus(raw_str).encode("utf-8")).hexdigest()
    return sn


def geo_coding(locations):
    uri = "/geocoder/v2/"
    uri_with_query_str = uri + "?location=%s&output=json&latest_admin=1&ak=%s" % (
        ",".join(map(str, locations)), settings.BAIDU_MAP_AK)
    url = _BAIDU_MAP_DOMAIN + uri_with_query_str + ("&sn=%s" % _generate_sn(uri_with_query_str))
    resp = requests.get(url)
    if resp.status_code == 200:
        resp_json = resp.json()
        if resp_json.get("status") == 0:
            return resp_json.get("result")
