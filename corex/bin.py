import requests , time , json
def bin_generator(bin , round):
    url = "https://www.vccgenerator.org/fetchdata/namso-generator/"
    cookie = {"csrftoken":"or3rib3nxPOPu6eLjTTbuhW2BahQXNSrnMfR8F4cfsDImPbxBXQLJQvxKGe3eRRA"}
    header = {"content-type":"application/x-www-form-urlencoded","X-Csrftoken":"m5neUA6NtNPVs5zuCq6Rys0ub9xo97gllqzEK47CbqEOkOwgUu3rN1zZkFuBqbfu"}
    payload = {"bin":bin,"quantity":int(round),"month":"random","year":"random","cvv":"","isDateChecked":True,"isCvvChecked":True,"ctoken":"m5neUA6NtNPVs5zuCq6Rys0ub9xo97gllqzEK47CbqEOkOwgUu3rN1zZkFuBqbfu"}
    req = requests.post(url , cookies=cookie , headers=header,data=payload).text
    data = json.loads(req)
    for i in data['data']:
        open("bin_generated.txt","a").write(str(i['card_number']) + "|" + str(i['expiration_date']) + '|' + str(i['cvv']) + "\n")
        
