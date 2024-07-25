from PyKakao import Message
API = Message(service_key="bfc4bd6ba10f9e4bdb90d5ba83501417")

auth_url = API.get_url_for_generating_code()
print(auth_url)