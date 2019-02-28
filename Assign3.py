import requests

def he_she_extract(x):
    H = []
    S = []
    
    for _ in range(x):
        r = requests.get('https://theyfightcrime.org/')
        p = r.text.split('<P>')
        
        she_loc  = p[1].find("She's")
        they_loc = p[1].find("They")
        
        H.append(p[1][5:she_loc].capitalize())
        S.append(p[1][(she_loc)+6:they_loc].capitalize())
        
    with open('HE.txt', 'w') as txt:
        txt.write('\n'.join(H))
        txt.close()
    
    with open('She.txt', 'w') as txt:
        txt.write('\n'.join(S))
        txt.close()   

he_she_extract(50)

