import re
paths=input("경로를 입력해주세요: ")
filenam=input("파일이름을 입력해주세요: ")
filepath=paths+'\\'+filenam+'.txt'
file=open(filepath,'r',encoding='UTF8')
data=file.readlines()
data_t=[]
count=[]
for ii in data:
    data_t.append(ii[:-1])
regex=re.compile(r'\d{5}(\w|\s)\w+')
for i in data_t:
    matchobj=regex.search(i)
    if matchobj!= None:
        stunum=matchobj.group()
        count.append(stunum)
count.sort()
comp=set(count)
comp=list(comp)
comp.sort()
for i in comp:
    print("%s의 채팅 수 : %d " %(i,count.count(i)))

while(1):
    exitq=input("종료를 원하시면 q버튼과 엔터를 눌러주세요")
    if exitq=='q':
        break
