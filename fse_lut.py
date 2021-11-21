
class table:
    def __init__(self,total):
        self.total = total
        self.dict = {}

    def genWithData(self,data):
        dataset = set(data)
        self.len = len(data)
        self.dict = {}
        cdf = 1
        for item in dataset:
            self.dict.update({item:(data.count(item),cdf)})
            cdf = cdf + data.count(item)
        print(self.dict)

data = "ybbybb010"
dataList = list(data)
t = table(8)
t.genWithData(dataList)
