import json

print("#################### Детерминированный конечный автомат ####################")

def read_json():
    with open('file.json') as f:
        templates = json.load(f)
    return templates['table']

table = read_json()

err=0
for i in range(len(table)):
    if table[i].get("triggers") == None:
        err+=1
    if table[i].get("source") == None:
        err+=1
    if table[i].get("dest") == None:
        err+=1
    if table[i].get("final") == None:
        err+=1
print("Ошибки json = ", err)

if err > 0:
    quit()

slov=[]
s = 0
for i in range(len(table)):
    if table[i].get("triggers") not in slov:
        slov.append(table[i].get("triggers"))

print("Алфавит автомата: ",slov)

print("Введите цепочку слова:")
chain = str(input())

for i in range(len(chain)):
    if chain[i] in slov:
        s+=1

if s!=len(chain):
    print("Цепочка слова неверна!")
    quit()

status = "0"
s = 0
print("####################")
for i in range(len(chain)):
    print("Символ: " + chain[i])
    print("Состояние: " + status)
    for j in range(len(table)):
        if chain[i] == table[j].get("triggers"):
            # print(chain[i],"-",table[j].get("triggers"))
            # print(status)
            if status == table[j].get("source"):
                if table[j].get("dest") != "none":
                    status = table[j].get("dest")
                    # print(status)
                if table[j].get("final") == "t":
                    # print("Success! The chain (" + chain + ") fits")
                    s = 1
                break
    print("Состояние: " + status)
    print("###########")
if s == 1:
    print("Success! The chain (" + chain + ") fits")
else:
    print("Fail")
