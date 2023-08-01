import json
import urllib.error
import urllib.parse
import urllib.request
def translate(sentence, src_lan, tgt_lan, apikey):
    url = 'http://api.niutrans.com/NiuTransServer/translation?'
    data = {"from": src_lan, "to": tgt_lan, "apikey": apikey, "src_text": sentence}
    data_en = urllib.parse.urlencode(data)
    req = url + "&" + data_en
    res = urllib.request.urlopen(req)
    res = res.read()
    res_dict = json.loads(res)
    if "tgt_text" in res_dict:
        result = res_dict['tgt_text']
    else:
        result = res
    return result
if __name__ == "__main__":
    in_src = open("./clean_data/cleaned_en_corpus.txt", "r", encoding='utf-8')
    out_src = open("./clean_data/cleaned_en_corpus.txt.big.test", "w", encoding='utf-8')
    lines = in_src.readlines()
    for line in lines:
        line = line.strip()
        print(line)
        trans = translate(line, 'en', 'zh', '8cb0f85de6970f0d1437c440c1fb0079')
        print(trans)
        try:
            trans = trans.decode('utf-8')
        except:
            trans = trans
        out_src.write(trans + "\n")

