#!/usr/bin/python
# text = []
# with open("text.txt", 'rb') as f:
#     symbs = f.read().splitlines()
#     for s in symbs:
#         print(s.decode("unicode_escape"))
#-------LEAD------ G GG N D DD R M B BB S SS - J JJ C K T P H
#-------VOWEL----- A AE YA YAE EO E YAE YE O WA WAE OE YO U WEO WE WI YU EU YI I
#-------TAIL------ G GG GS N NJ NH D L LG LM LB LS LT LP LH M B BS S SS NG J C K T P H

lookup = {"lead":['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ',
                 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'],
          "lead_phon": ['G', 'GG', 'N', 'D', 'DD', 'R', 'M', 'B', 'BB', 'S', 'SS', '-', 'J', 'JJ', 'C', 'K', 'T', 'P', 'H'],
          "vowel": ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ',
                    'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ'],
          "vowel_phon": ['A', 'AE', 'YA', 'YAE', 'EO', 'E', 'YAE', 'YE', 'O', 'WA', 'WAE', 'OE', 'YO', 'U', 'WEO', 'WE', 'WI', 'YU', 'EU', 'YI', 'I'],
          "tail":['ㄱ', 'ㄲ', 'ᆪ', 'ㄴ', 'ᆬ', 'ᆭ','ㄷ', 'ㄹ', 'ᆰ', 'ᆱ', 'ᆲ',
                  'ᆳ', 'ᆴ', 'ᆵ', 'ᆵ', 'ㅁ', 'ㅂ', 'ᆹ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ',
                  'ᆽ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'],
          "tail_phon": ['G', 'GG', 'GS', 'N', 'NJ', 'NH', 'D', 'L', 'LG', 'LM', 'LB', 'LS', 'LT', 'LP', 'LH', 'M', 'B', 'BS', 'S', 'SS', 'NG', 'J', 'C', 'K', 'T', 'P', 'H'],
}



# consonant_map = {'ㄱ': ('g','k'), 'ㄲ': ('kk', 'k'), 'ㄴ': ('n'), 'ㄷ': ('d', 't'),
#                  'ㄸ': ('tt', '-'), 'ㄹ': ('r', 'l'), 'ㅁ': ('m'), 'ㅂ': ('b', 'p'),
#                  'ㅃ': ('pp', '-'), 'ㅅ': ('s', 't'), 'ㅆ': ('ss', 't'),
#                  'ㅇ': ('-', 'ng'), 'ㅈ': ('j', 't'), 'ㅉ': ('jj', '-'),
#                  'ㅊ': ('ch', 't'), 'ㅋ': ('k'), 'ㅌ': ('t'), 'ㅍ': ('p'), 'ㅎ': ('h', 't')}
#
# vowel_map = {'ㅏ': 'a', 'ㅐ': 'ae', 'ㅑ': 'ya', 'ㅒ': 'yae', 'ㅓ': 'eo', 'ㅔ': 'e',
#              'ㅕ': 'yeo', 'ㅖ': 'ye', 'ㅗ': 'o', 'ㅘ': 'wa', 'ㅙ': 'wae', 'ㅚ': 'oe',
#              'ㅛ': 'yo', 'ㅜ': 'u', 'ㅝ': 'wo', 'ㅞ': 'we', 'ㅟ': 'wi', 'ㅠ': 'yu',
#              'ㅡ': 'eu', 'ㅢ': 'ui', 'ㅣ': 'i'}
words = ['서','있','다', '서', '울', '사', '람']
for s in words:
    cp = ord(s) # codepoint
    print("")
    print("Word:", s)
    tail = (cp - 44032) % 28 - 1
    vowel = 1 + int(((cp - 44032 - tail) % 588)/28) - 1
    lead = 1 + int((cp-44032)/588) - 1

    if tail < 0:
        tm = ""
        tmph = ""
    else:
        tm = lookup["tail"][tail]
        tmph = lookup["tail_phon"][tail]

    if vowel < 0:
        vm = ""
        vmph = ""
    else:
        vm = lookup["vowel"][vowel]
        vmph = lookup["vowel_phon"][vowel]

    if lead < 0:
        lm = ""
        lmph = ""
    else:
        lm = lookup["lead"][lead]
        lmph = lookup["lead_phon"][lead]

    print("Lead", lm, lmph)
    print("Vowel", vm, vmph)
    print("Tail", tm, tmph)
