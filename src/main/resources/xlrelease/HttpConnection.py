class HttpConnection:
    def __init__(self, url, username = None, password = None, proxyHost = None, proxyPort = None):
        self.username = username
        self.password = password
        self.url = url
        self.proxyHost = proxyHost
        self.proxyPort = proxyPort

    def getUrl(self):
        return self.url

    def getProxyHost(self):
        return self.proxyHost

    def getProxyPort(self):
        return self.proxyPort

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password