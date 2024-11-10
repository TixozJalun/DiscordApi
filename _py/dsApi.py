import requests

class api:
    # Данные для отправки сообщения
    def __init__(self, token, key, vers):
        self.headers = {
            "accept": "*/*",
            "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            "authorization": token,
            "priority": "u=1, i",
            "sec-ch-ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "ru",
            "x-discord-timezone": "Europe/Moscow",
            "x-super-properties": key
        }
        self.vers = vers
    
    # Даёт список сообщений в виде json объекта
    def getMsg(self, channel, point, lenMsg):
        url = f"https://discord.com/api/{self.vers}/channels/{channel}/messages?before={point}&limit={lenMsg}"
        return requests.get(url, headers=self.headers).json()
    
    # Удаляет указанное вами сообщение
    def delMsg(self, channel, point):
        url = f"https://discord.com/api/{self.vers}/channels/{channel}/messages/{point}"
        requests.delete(url, headers=self.headers)
    
    # Выдаёт данные о профиле пользователя
    def getPfl(self, user):
        url =  f"https://discord.com/api/{self.vers}/users/{user}/profile?with_mutual_guilds=false&with_mutual_friends=true&with_mutual_friends_count=false"
        return requests.get(url, headers=self.headers).json()

    # Ставить реакцию на сообщение.
    def putRct(self, cnl, point, rct, rctNam):
        url = f"https://discord.com/api/{self.vers}/channels/{cnl}/messages/{point}/reactions/{rctNam}%3A{rct}/%40me?location=Message%20Hover%20Bar&type=0"
        requests.put(url, headers=self.headers)

    # Убрать реакцию на сообщение.
    def delRct(self, cnl, point, rct, rctNam):
        url = f"https://discord.com/api/{self.vers}/channels/{cnl}/messages/{point}/reactions/{rctNam}%3A{rct}/0/%40me?location=Message%20Inline%20Button&burst=false"
        requests.delete(url, headers=self.headers)

    # Отправление сообщения.
    def pstMsg(self, cnl, msg, rnd):
        url = f"https://discord.com/api/{self.vers}/channels/{cnl}/messages"
        data = {
            "mobile_network_type":"unknown",
            "content":msg,
            "nonce": rnd,
            "tts":False,
            "flags":0
        }
        return requests.post(url, headers=self.headers, json=data)

    # Список каналов.
    def getSrv(self, srv):
        url = f"https://discord.com/api/{self.vers}/guilds/{srv}/entitlements?"
        return requests.get(url, headers=self.headers).json()
    
    def cntSrv(self, url, rnd):
        data = {"session_id":rnd}
        requests.post(url, headers=self.headers, json=data)

"https://discord.com/api/v9/activities/shelf?guild_id=1262787644111458436"
"https://discord.com/api/v9/channels/1215233394569379901/threads/search?archived=true&sort_by=last_message_time&sort_order=desc&limit=25&tag_setting=match_some&offset=0"
"https://discord.com/api/v9/guilds/664844827497594883/application-command-index"
""