class MYDB:
    def __init__(self, server):
        self.server = server
        self.conn = Connect(self.server)

    def connect(self):
        return self.conn


class Connect:
    def __init__(self, server):
        self.server = server
        self.cur = Cur

    def cur(self):
        return self.cur
    def close(self):
      pass


class Cur:
    def __init__(self, query):
        self.query = query

    def feature(self):
        return Feature(self.query)


class Feature:
    def __init__(self, query):
        self.query = query

    def get(self):
        if self.query == "Tom":
            print({"name": "Tom cruise", "num": "090836353", "state": "Kaduna"})
            return 1
        if self.query == "Mark":
            print({"name": "Mark Zuckerburg", "num": "0908353--", "state": "Lagos"})
            return 1
