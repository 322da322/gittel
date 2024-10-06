import requests, uuid, json
import config
client_id = config.sberID
secret = config.sberSC
auth = config.sberAU
def get_token1(auth_token, scope='GIGACHAT_API_PERS'):
  rq_uid = str(uuid.uuid4())
  url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

  headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Accept': 'application/json',
      'RqUID': rq_uid,
      'Authorization': f'Basic {auth_token}'
  }
  payload={
      'scope': scope
  }
  try:
    response = requests.post(url, headers=headers, data=payload, verify=False)
    giga_token = response.json()['access_token']
    return giga_token
  except requests.RequestException as e:
    return -1
def get_chat_completion(auth_token, user_message):  
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
    payload = json.dumps({
                "model": "GigaChat" ,
                "messages": [
                    {
                       "role": "user", 
                       "content": user_message 
                  }],
               "temperature": 1, 
                "top_p": 0.1,  
                "n": 1,  
                "stream": False,
                "max_tokens": 512, 
             "repetition_penalty": 1,
             "update_interval": 0  
          })
    headers = {
                'Content-Type': 'application/json',  # Тип содержимого - JSON\n",
                'Accept': 'application/json',  # Принимаем ответ в формате JSON\n",
                'Authorization': f'Bearer {auth_token}'  # Токен авторизации\n",
            }
    try:
        response = requests.request("POST", url, headers=headers, data=payload, verify=False)
        return response
    except requests.RequestException:
        return -1
#answer = get_chat_completion(get_token1(auth), 'Пример задачи по математике огэ')
#print("----------------")
#print(answer.json()['choices'][0]['message']['content'])