import fse_lut

class fse:
    def __init__(self,data,ls):
        self.ls = ls
        table = fse_lut.table(ls)
        datalist = list(data)
        table.genWithData(datalist)
        self.table = table.table
        
    def encode(self,data):
        output = 0
        state = self.ls
        for d in data:
            gettable = self.table[d][state-self.ls]
            state = gettable[1]
            for updateOut in gettable[0]:
                output = output << 1 + updateOut
        output = output * self.ls + state
        return output

    def decode(self,data):
        div,state = divmod(data,self.ls)
        data = div * self.ls
        while (state != self.ls) or (data != 0):
            print()

data = "ybbybb010"
fse = fse(data,16)
enc = fse.encode(data)
print(enc)
