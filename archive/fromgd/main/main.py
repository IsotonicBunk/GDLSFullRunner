import requests
import json
import base64
from random import randint
from time import ctime, sleep

BACKUP_FREQ = 10000

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

def kv_to_json(text: str) -> str:
    parts = text.split(':')

    if len(parts) % 2 != 0:
        raise ValueError("An error occured when converting key:valuse to json. text:" + text)
        #return {
        #    'nan':text
        #}

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
    
def get_info(level_id):
    url = f"https://gdbrowser.com/api/level/{level_id}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        
        data = response.json()
        return data
    
    except requests.exceptions.RequestException as e:
        print(e)
        return
    except json.JSONDecodeError:
        print(response)
        return


def get_info_author(author, page):
    url = f"https://gdbrowser.com/api/search/{author}?page={page}&count=10&user"

    try:
        response = requests.get(url)
        response.raise_for_status()

        # print(response)
        levels = response.json()

        # print(levels)
        result = [i['id'] for i in levels]
        print(f'Response: {response}\nAuthor: {author}\nLevel: {level["id"]}')
        return (result, levels)
    
    except requests.exceptions.RequestException as e:
        print(f'Failed to find level {e}\nResponse: {response}\nAuthor: {author}\nLevel: {level["id"]}')
        return
    except json.JSONDecodeError:
        print(response.json())
        return

# while True:
#     level = None
#     while True:
#         level = get_info(randint(128, 117979939))
#         if level != None:

#             level_author = get_info_author(level['author'], 0)
#             if level_author == None:
#                 continue
#             level_author = level_author[1]
#             levels=[]
#             for i in range(int(level_author[0]['pages'])):
#                 levels.extend(get_info_author(level['author'], i)[0])

#             if level['id'] not in levels:
#                 print(level['id'], levels)
#                 break
#             else:
#                 pass
#                 # print(f"PUBLIC {level['name']} by {level['author']}\nLikes: {level['likes']}\nDownloads: {level['downloads']}\nObjects: {level['objects']}\nLen: {len(levels)}\n{level['id']}\n")

# i = 118026371
# for j in range(10000):
#     i -= 1
#     level = get_info(i)
#     if level != None:
#         if level['author'] == 'Tttn324':
#             print(f"LESSS GO WE FIND ID\n\n{level['name']} by {level['author']}\nLikes: {level['likes']}\nObjects: {level['objects']}\nDownloads: {level['downloads']}\n{level['id']}\n\n")
#             break
#         print(f"{level['name']} by {level['author']}\nLikes: {level['likes']}\nObjects: {level['objects']}\nDownloads: {level['downloads']}\n{level['id']}\n\n!!!")

data = {}
data_cl = {}
exist_levels = []

try:
    with open('data.json', 'r', encoding='utf-8') as f:
        file = f.read()
        data = json.loads(file)
        print(f'Data successfully loaded (len is {len(data.keys())})')
except:
    print('data.json is not found')
    with open('data.json', 'w', encoding='utf-8') as f:
        f.write("")
        data = {}

try:
    with open('data-temp.json', 'r', encoding='utf-8') as f:
        file = f.read()
        data_cl = json.loads(file)
        print(f'Data temp successfully loaded (len is {len(data_cl.keys())})')
except:
    print('data-temp.json is not found')
    with open('data-temp.json', 'w', encoding='utf-8') as f:
        f.write("")
        data_cl = {}

try:
    with open('exist-levels.json', 'r', encoding='utf-8') as f:
        file = f.read()
        exist_levels = json.loads(file)
        print(f'Exist levels successfully loaded (len is {len(exist_levels)})')
except:
    print('exist-levels.json is not found')
    with open('exist-levels.json', 'w', encoding='utf-8') as f:
        f.write("")
        exist_levels = []

try:
    with open('data.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps({**data, **data_cl}))
        print(f'Data and data temp successfully merged (len is {len(data.keys()) + len(data_cl.keys())})')
    with open('data-temp.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps({}))
except: pass


old_data_len = len(data.keys()) + len(data_cl.keys())
data_cl = {}
downloadTries = 0

while True:
    if downloadTries == 20:
        print("You sent 20 requests. Cooldown for 61 seconds...")
        for i in range(6):
            sleep(10)
            i -= 10
            print(i + "seconds remaining")
        sleep(1)
        print("Cooldown ended!")
    downloadTries += 1
    try:
        id = randint(128, 118028738)
        if str(id) in data.keys() or str(id) in data_cl.keys():
            print(f'ID {id} is already exist')
            exist_levels.append(id)
            with open('exist-levels.json', 'w', encoding='utf-8') as f:
                f.write(json.dumps(exist_levels))
            continue
        level = renameGdLevelKeys(kv_to_json(getRawDataFromId(id)))
        if level != None:
            data_cl[level['id']] = level
            print('<', end='')
            with open('data-temp.json', 'w', encoding='utf-8') as f:
                f.write(json.dumps(data_cl))
            print('>')
            print(f'\nData length: {len(data_cl.keys()) + old_data_len} ({len(data_cl.keys())})\n')
            print(f"""[{ctime()}]\n{level['name']} by {level['playerID']} (creator's player ID)
        
Likes: {level['likes']}
Downloads: {level['downloads']}
Objects: {level['objects']}
Version: {level['gameVersion']}
{level['id']}
    """)
        else:
            data_cl[id] = None
            print(f'ID {id} is not exist ({len(data_cl.keys()) + old_data_len})')
        if (len(data_cl.keys()) + old_data_len) % BACKUP_FREQ == 0 or (len(data_cl.keys()) + old_data_len) == 1390420:
            with open(f'bckp\data ({len(data_cl.keys()) + old_data_len}) (auto).json', 'w', encoding='utf-8') as f:
                f.write(json.dumps({**data, **data_cl}))
            print(f'Data and data temp successfully merged (len is {len(data.keys()) + len(data_cl.keys())})')

    except Exception as e:
        print(ctime(), e)
    # input()