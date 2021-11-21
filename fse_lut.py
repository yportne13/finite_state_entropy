
class table:
    def __init__(self,ls):
        self.ls = ls
        self.dict = {}
        self.table = {}

    def genWithData(self,data):
        dataset = set(data)
        self.len = len(data)
        self.dict = {}
        cdf = 1
        for item in dataset:
            self.dict.update({item:(data.count(item),cdf)})
            cdf = cdf + data.count(item)
        print(self.dict)
        self.gentable()
        for item in self.table:
            print(item,self.table[item])

    def shortState(self,toOutput,ls,item):
        (div,mod) = divmod(ls,self.dict[item][0])
        nextstate = self.ls*div + mod + self.dict[item][1]
        if nextstate > 2*self.ls - 1:
            toOutput.append(ls&0x01)
            return self.shortState(toOutput,ls>>1,item)
        else:
            return nextstate


    def gentable(self):
        for item in self.dict:
            table = []
            for l in range(self.ls):
                toOutput = []
                ls = l + self.ls
                state = self.shortState(toOutput,ls,item)
                table.append((toOutput,state))
            self.table.update({item:table})

data = "ybbybb010"
dataList = list(data)
t = table(10)
t.genWithData(dataList)
