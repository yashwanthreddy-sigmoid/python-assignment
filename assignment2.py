class Logger:
    def __init__(self):
        self.dict = {}

    def shouldPrintMessage(self,time_stamp,message):


        if message in self.dict.keys():
            if time_stamp >= self.dict[message]:
                print('true')
                self.dict[message] += 10
            else:
                print('false')

        else:
            print('true')
            self.dict[message]=time_stamp+10




input1 =[[1,'foo'],[4,'bar'],[3,'foo'],[8,'bar'],[10,'foo'],[11,'foo']]

obj = Logger()
for i in range(len(input1)):
    obj.shouldPrintMessage(input1[i][0],input1[i][1])



