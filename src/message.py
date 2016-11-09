import datetime
import json
'''
request format:
| method | path | 
| server: | fqdn
| header: | value <-- followed by \n\n
|  ???? encoded message #TODO
'''


class request(object):
    def __init__(self, msg):
        lines = msg.split("n")
        self.method, self.path, self.proto = lines[0].split()
        try:
            self.data = json.loads(lines[len(lines) - 1])
        except:
            self.data = {'data': 'none'}


class response(object):
    format = "%d %"  #TODO

    def __init__(self):
        self.proto = "HTTP/1.1"
        self.code = 200
        self.message = "OK"
        self.headers = "Server: wumpusd\nContent-Type: text/json; charset=UTF-8\n\n"
        self.data = ""

    def __str__(self):
        now = datetime.datetime.today()
        dt = now.strftime(self.format)
        return self.proto + " " + str(self.code) + " " + self.message + \
        "\nDate: " + dt + "\n" + self.headers + json.dumps(self.data)
