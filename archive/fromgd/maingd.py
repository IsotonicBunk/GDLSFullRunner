import requests
import json
import base64



def getRawDataFromId(id) :
    url = 'http://www.boomlings.com/database/downloadGJLevel22.php'
    headers = {'user-agent': '', 'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'gameVersion': '22','binaryVersion':'35','gdw':'0','levelID':id,'secret':'Wmfd2893gb7'}

    r = requests.post(url, headers=headers, data=payload)
    return r.text



def getUserInfo(userId) :
    url = 'http://www.boomlings.com/database/getGJUserInfo20.php'
    headers = {'user-agent': '', 'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'gameVersion': '22','binaryVersion':'35','gdw':'0','targetAccountID':userId,'secret':'Wmfd2893gb7'}

    r = requests.post(url, headers=headers, data=payload)
    return r.text


#i = 0
#print("Введите ID уровня:")
#while (i < 51):
#    i += 1
#    print(
#    
#    )

def kv_to_json(text: str) -> str:
    parts = text.split(':')

    if len(parts) % 2 != 0:
        raise ValueError("Нечётное количество элементов, пары key:value нарушены")

    data = {parts[i]: parts[i+1] for i in range(0, len(parts), 2)}
    #return json.dumps(data, ensure_ascii=False, indent=2)
    return data
def renameGdLevelKeys(oldJson):
    oldJson = checkForMissingGdLevelKeys(oldJson)
    oldJson["3"] = base64.b64decode(oldJson["3"]).decode('utf-8')
    newJson = {
        'id': oldJson["1"],
        'name': oldJson["2"],
        'description': oldJson["3"],
        'version': oldJson["5"],
        'playerID': oldJson["6"],
        'difficultyDenominator': oldJson["8"],
        'difficultyNumerator': oldJson["9"],
        'downloads': oldJson["10"],
        'setCompletes': oldJson["11"],
        'officialSong': oldJson["12"],
        'gameVersion': oldJson["13"],
        'likes': oldJson["14"],
        'length': oldJson["15"],
        'dislikes': oldJson["16"],
        'demon': oldJson["17"],
        'stars': oldJson["18"],
        'featureScore': oldJson["19"],
        'auto': oldJson["25"],
        'recordString': oldJson["26"], 
        'password': oldJson["27"],
        'uploadDate': oldJson["28"],
        'updateDate': oldJson["29"],
        'copiedID': oldJson["30"],
        'twoPlayer': oldJson["31"],
        'customSongID': oldJson["35"],
        'extraString': oldJson["36"],
        'coins': oldJson["37"],
        'verifiedCoins': oldJson["38"],
        'starsRequested': oldJson["39"],
        'lowDetailMode': oldJson["40"],
        'dailyNumber': oldJson["41"],
        'epic': oldJson["42"],
        'demon Difficulty': oldJson["43"],
        'isGauntlet': oldJson["44"],
        'objects': oldJson["45"],
        'editorTime': oldJson["46"],
        'editorTime(Copies)': oldJson["47"],
        'settingsString': oldJson["48"],
        'songIDs': oldJson["52"],
        'sfxIDs': oldJson["53"],
        'unknown': oldJson["54"],
        'verificationTime': oldJson["57"]
            
        }    

    return newJson

def checkForMissingGdLevelKeys(trgJson): # шо за дебильное название
    checkedJson = trgJson
    tmpKey = 0 
    while tmpKey < 58:
        tmpKey = tmpKey + 1
        if str(tmpKey) in trgJson:
            pass
        else:
            checkedJson[str(tmpKey)] = ''
    return checkedJson
    

#levelData = renameGdLevelKeys(kv_to_json(getRawDataFromId(-1)))


#print(levelData)

#print(getUserInfo(7244751))
        


