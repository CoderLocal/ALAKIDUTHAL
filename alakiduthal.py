import math
#Aasiriyapa Function
def paa_vagai(Lines,linenum):
    eetrasai=Lines[-1].split(" ")[-1][-1 : -3]
    #bool = eetrasai =='ய்' or eetrasai not in kuril_eluthu and eetrasai not in uyir_mei_eluthu
    if(linenum>2):
        s,ind=[],0
        for i in lines:
            s.append(len(Lines[ind].split(" ")))
            ind+=1
        print(s)
        if(s[0]+s[-1]==8 ):
            if(s==[4]*linenum):
                print("நிலைமண்டில ஆசிரியப்பா")
            elif(s[-3]<4):
                print("இணைக்குறள் ஆசிரியப்பா")
            else:
                print("நேரிசை ஆசிரியப்பா")
        else:
            print("Not a Aasiriyappa")
def lineExtraction(string):
    lineNum=0
    lines=[]
    paatuLines=string.split("\n")
    for sol in paatuLines:
        if sol.strip()!="":
            lines.append(sol.strip())
    return lines
def print_alagu(seer):
    table = []
    if len(seer) > 1 and seer[0] == "0":
        table.append(alagu[seer[0]])
        table.extend(print_alagu(seer[1:]))
    elif (len(seer) > 2) and seer[2] == "1":
        table.append(alagu[seer[:2]])
        table.extend(print_alagu(seer[2:]))
    elif (len(seer) > 2) and seer[2] == "0":
        table.append(alagu[seer[:2]])
        table.extend(print_alagu(seer[2:]))
    else:
        table.append(alagu[seer])
    return table
def split_mei(word):
    seer, start = [], 0
    count = 0
    # iterates the word using index
    for index in range(len(word)):
        # print(seer)
        if word[index] == "்":
            seer.append(word[start:index - 1])
            # print(seer,start)
            start = index + 1
            count =0
        #  to add last 'சீர்'  if it does not end with 'மெய்யெழுத்துக்கள்'
        elif  is_not_kuril(word[index]) :
            # print(start)
            seer.append(word[start:index+(count == 0)])
            start = index+1
            count = 0
        if count ==2 and is_kuril(word[index]):
            #  print(start,word[index])
             seer.append(word[start:index])
             start = index
             count =0
        if is_kuril(word[index]):
            count+=1
        if index == len(word) - 1 :
            for i in word[start:]:
                if i not in mei_eluthu:
                    seer.append(word[start:])
                    break
    return seer

nedil = ['ஆ','ஈ','ஊ','ஏ','ஐ','ஓ']
kuril_eluthu = ['அ', 'இ', 'உ', 'எ', 'ஒ', 'க', 'ங', 'ச', 'ஞ', 'ட', 'ண', 'த', 'ந', 'ப', 'ம', 'ய', 'ர', 'ல', 'வ', 'ழ', 'ள',
                'ற', 'ன']
uyir_mei_eluthu = ['ி', 'ு', 'ெ', 'ொ']
nedil = ['ஆ	','ஈ','ஊ','']
alagu = {'1': "நேர்", "0": "நேர்", "10": "நிரை ", "11": "நிரை ", "110": "நிரை"}
mei_eluthu=['க்', 'ங்', 'ச்', 'ஞ்', 'ட்', 'ண்', 'த்', 'ந்', 'ப்', 'ம்', 'ய்', 'ர்', 'ல்', 'வ்', 'ழ்', 'ள்','ற்', 'ன்']
def is_kuril(letter):
    return letter in kuril_eluthu


def is_uyir_mei(letter):
    return letter in uyir_mei_eluthu

def is_not_kuril(letter):
    return not( letter in kuril_eluthu or letter in uyir_mei_eluthu)
seer_asai = {
    "1": "நாள்",
    "2": "மலர்",
    "11":"தேமா",
    "12":"கூவிளம்",
    "21":"புளிமா",
    "22":"கருவிளம்",
    "111":"தேமாங்காய்",
    "112":"தேமாங்கனி",
    "121":"கூவிளங்காய்",
    "122":"கூவிளங்கனி",
    "211":"கருவிளங்காய்",
    "212":"புளிமாங்கனி",
    "221":"கருவிளங்காய்",
    "222":"கருவிளங்கனி"
}
d = {
    "1":"நேர்",
    "2":"நிரை"
}
def count(asai):
    c =0
    for i in asai:
        if i in kuril_eluthu or i in nedil :
            c+=1
    return str(c)
def enco(word):
        enc=""
        asai = split_mei(word)
        while '' in asai:
            asai.remove('')
        while ' ' in asai:
            asai.remove(' ')
        print
        for i in asai:
            enc+=count(i)
        return str(enc)
def decode(asai):
    str=""
    for i in asai:
        str+=d[i]
    return str

def value(pathigam):
    res = []
    for line in (lineExtraction(pathigam)):
        ans=[]
        words = line.split(" ")
        while '' in words:
            words.remove('')
        while ' ' in words:
            words.remove(" ")
        # print(words)
        for word in words:
            if(word != '' and word != ' '):
                ans.append(enco(word))
                # print(word,enco(word),split_mei(word))
        # res.append(list(map(decode,seers)))
        res.append(ans)
    return res

