# soundcloud-rpc
<h1>SoundCloudで再生中の曲をDiscordで表示することができます。<h1>
<h2>Support Discord @np8_j</h2>
<img src="https://cdn.discordapp.com/attachments/1225794966081638461/1235984585834233937/image.png?ex=66365bd8&is=66350a58&hm=72e9be8e132d4f661ccd918c7408fcffe843e1e803274a80fd3c55b9426d0078&"/>

<h1>App IDの取得方法はさすがに自分で調べてください、、、</h1>

<h1>SoundCloudのOAuth Token & Client_IDの取得方法</h1>
<h2>(https://soundcloud.com/discover) にアクセス</h2>
<p>開いたらF12 or Ctrl + Shift + Iを同時押し</p>
<img src="https://github.com/cocoapc911/soundcloud-rpc/assets/127626229/f4d83b1d-c59a-415b-be03-18f96041a16e"/>
<p>この部分にapiと入力しEnterキーで検索開始</p>
<img src="https://github.com/cocoapc911/soundcloud-rpc/assets/127626229/01625dc1-8bc1-4a97-8ce7-d383d85aec48"/>
<p>一番上に出てきた通信をクリック、Request URL:の中にclient_idが隠れているので&の部分までclientidをコピー</p>
<p>Oauth TokenはRequest HeadersのAuthorization:の中にあります</p>
