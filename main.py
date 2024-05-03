from sound_cloud_api import Soundcloud
from pypresence import Presence
import time

#Discord Developer Portalで作成したApp ID
app_id = 123456789
#SoundCloudで取得したOAuth TokenとClient_id
oauth2,client_id = "OAuthから始まるToken(OAuthという文字も含めます)","Sound_cloudのClient_id"

account = Soundcloud(f"{oauth2}", f"{client_id}")
RPC = Presence(int(app_id)) 
RPC.connect()
sound_cloud_image = "https://d21buns5ku92am.cloudfront.net/26628/images/419679-1x1_SoundCloudLogo_cloudmark-f5912b-large-1645807040.jpg"

def null_check(res):
    if res == "":return False
    else:return True

def get_info():
    json_data = account.get_now()
    nowtime = time.time()
    title,descriptions,image,username= json_data["title"],json_data["description"],json_data["artwork_url"],json_data["user"]["username"]
    if not null_check(descriptions):
        descriptions ="概要はありません。"
    if not null_check(image):
        image ="https://d21buns5ku92am.cloudfront.net/26628/images/419679-1x1_SoundCloudLogo_cloudmark-f5912b-large-1645807040.jpg"
    if not null_check(username):
        username ="Noname"
    return [descriptions,title,image,username,nowtime]

def rpc_start(descriptions,title,image,username,nowtime):
    try: 
        RPC.update(state=f"{descriptions[0:100]}", details=f"{title}",large_image=f"{image}",large_text=f"User: {username}",small_text=f"Created By @np8_j",start=nowtime,small_image=f"{sound_cloud_image}")
        time.sleep(80)
        json_data = account.get_now()
        title2 = json_data["title"]
        if title == title2:
            rpc_start(descriptions,title,image,username,nowtime,sound_cloud_image)
    except:pass
    
while True:
    data = get_info()
    rpc_start(descriptions=data[0],title=data[1],image=data[2],username=data[3],nowtime=data[4])