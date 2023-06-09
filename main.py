# -*- coding: utf-8 -*-

from os import getenv
from pandora_cloud_twist.server import ChatBot

# import requests
# revoke fresh token, access_token 是通过 fresh token 来刷新的
# 如果 fresh token 被泄漏了，可以通过下面的接口来 revoke
# client_id 是一个 plugin client id（我理解的）
# response = requests.post("https://auth0.openai.com/oauth/revoke", data={"client_id": "pdlLIX2Y72MIl2rhLhTE9VV9bN905kBh", "token": "TQfWxLSDocJzAIk77u3YRa1gS_vIxwRco4O9U9fZSSar5"})
# print(f"{response}")
# 有关 openai 的其他 auth 接口实现代码，查看 pandora/openai/auth.py 文件
# access_token 的技术原理: https://zhile.io/2023/05/19/how-to-get-chatgpt-access-token-via-pkce.html

_port = getenv('PORT')
_proxy = getenv('PANDORA_PROXY')
_debug = getenv('PANDORA_DEBUG', 'false').lower() == 'true'
_sentry = getenv('PANDORA_SENTRY', 'false').lower() == 'true'
_listen = getenv('PANDORA_SERVER_LISTEN', 'true').lower() == 'true'
_server = getenv('PANDORA_SERVER', '0.0.0.0:{}'.format(_port) if _port else '0.0.0.0')

app = ChatBot(proxy=_proxy, debug=_debug, sentry=_sentry, login_local=True).run(_server, listen=_listen)
