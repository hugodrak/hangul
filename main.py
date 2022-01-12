import random
import time
import os
consonant_map = {'ㄱ': ('g','k'), 'ㄲ': ('kk', 'k'), 'ㄴ': ('n'), 'ㄷ': ('d', 't'),
                 'ㄸ': ('tt', '-'), 'ㄹ': ('r', 'l'), 'ㅁ': ('m'), 'ㅂ': ('b', 'p'),
                 'ㅃ': ('pp', '-'), 'ㅅ': ('s', 't'), 'ㅆ': ('ss', 't'),
                 'ㅇ': ('-', 'ng'), 'ㅈ': ('j', 't'), 'ㅉ': ('jj', '-'),
                 'ㅊ': ('ch', 't'), 'ㅋ': ('k'), 'ㅌ': ('t'), 'ㅍ': ('p'), 'ㅎ': ('h', 't')}

vowel_map = {'ㅏ': 'a', 'ㅐ': 'ae', 'ㅑ': 'ya', 'ㅒ': 'yae', 'ㅓ': 'eo', 'ㅔ': 'e',
             'ㅕ': 'yeo', 'ㅖ': 'ye', 'ㅗ': 'o', 'ㅘ': 'wa', 'ㅙ': 'wae', 'ㅚ': 'oe',
             'ㅛ': 'yo', 'ㅜ': 'u', 'ㅝ': 'wo', 'ㅞ': 'we', 'ㅟ': 'wi', 'ㅠ': 'yu',
             'ㅡ': 'eu', 'ㅢ': 'ui', 'ㅣ': 'i'}
#print("\t".join(vowel_map.keys()))
#print("\t".join([x[1] for x in vowel_map.items()]))
count = 0
corr = 0
done = []
t1 = time.time()
prev = ""
while True:
    #os.system('clear')
    #print(prev)

    keys = list(vowel_map.keys())
    i = random.randint(0, len(keys)-1)
    if i in done:
        if len(done) == len(keys):
            print('Time:', int(time.time() - t1), 's')
            break

        continue
    count += 1
    lett = vowel_map[keys[i]]
    print(keys[i])
    ans = input('=> ')
    prev = ""
    if ans == lett:
        done.append(i)
        corr += 1
        prev += '👍 ' + f'{int((corr*100)/count)}%'
    else:
        print("fail! Correct:", lett)
        break
        prev += '👎 ' + lett
    prev += "\n"
    print(prev)
