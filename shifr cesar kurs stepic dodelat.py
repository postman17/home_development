asd=int(input())
stroka=input()

class cesar:
    def shifr(self,asd,stroka):
        daq=''
        dq=' abcdefghijklmnopqrstuvwxyz'
        stroka=stroka.strip(' ')
            
        for x in stroka:
            af=dq.index(x)
            if asd>0:
                if (af+asd)>len(dq):
                    c=(af+asd)-len(dq)
                    daq+=dq[c]
                else:
                    daq+=dq[af+asd]
            else:
                if (af+asd)<0:
                    c=len(dq)+(af+asd)
                    daq+=dq[c]
                else:
                    daq+=dq[af+asd]  
        return daq
dfg=cesar()
print('Result: '+'"'+dfg.shifr(asd,stroka)+'"')
