def read():

    f=open("./data.txt","r",encoding="utf-8")

    read=f.readlines()
    # print(read)
    list=[]
    list1=[]

    for i in read:
        list.append(i.lstrip().split()[0])

    for m in list:
        n=tuple(m.split(","))

        list1.append(n)

    # print(list1)
    return list1
read()