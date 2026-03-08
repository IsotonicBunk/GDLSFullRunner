import requests



def getRawDataFromId(id) :
    url = 'http://www.boomlings.com/database/downloadGJLevel22.php'
    headers = {'user-agent': '', 'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'gameVersion': '22','binaryVersion':'35','gdw':'0','levelID':id,'secret':'Wmfd2893gb7'}

    r = requests.post(url, headers=headers, data=payload)
    return r.text

i = 0
#print("Введите ID уровня:")
while (i < 51):
    i += 1
    print(
    
    )
    
print(getRawDataFromId(input("Введите ID уровня: ")))
input("Нажмите Enter для завершения программы... ")