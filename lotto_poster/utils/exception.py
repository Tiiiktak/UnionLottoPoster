
class CrawlerException(Exception):
    def __init__(self, message, status_code=500):
        self.message = message
        self.status_code = status_code

    def __str__(self):
        return self.message
