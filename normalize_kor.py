from typing import List, Dict, Tuple, Union
from provisions import get_provision
lookup_1 = {"lead":       ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'],
          "lead_phon":  ['G', 'GG', 'N',  'D', 'DD', 'R', 'M', 'B', 'BB', 'S', 'SS', '',  'J', 'JJ', 'CH',  'K', 'T', 'P',  'H'],
          "vowel":      ['ㅏ', 'ㅐ', 'ㅑ',  'ㅒ',  'ㅓ',  'ㅔ', 'ㅕ',  'ㅖ', 'ㅗ', 'ㅘ',  'ㅙ',  'ㅚ',  'ㅛ', 'ㅜ', 'ㅝ',  'ㅞ',  'ㅟ',  'ㅠ', 'ㅡ',  'ㅢ', 'ㅣ'],
          "vowel_phon": ['A', 'AE', 'YA', 'YAE', 'EO', 'E', 'YEO', 'YE', 'O', 'WA', 'WAE', 'OE', 'YO', 'U', 'WEO', 'WE', 'WI', 'YU', 'EU', 'YI', 'I'],
          "tail":       ['ㄱ', 'ㄲ', 'ᆪ', 'ㄴ', 'ᆬ',  'ᆭ', 'ㄷ', 'ㄹ', 'ᆰ', 'ᆱ', 'ᆲ',  'ᆳ',  'ᆴ', 'ᆵ', 'ᆵ',  'ㅁ', 'ㅂ', 'ᆹ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ᆽ', 'ㅋ','ㅌ', 'ㅍ', 'ㅎ'],
          "tail_phon":  ['G', 'GG', 'GS', 'N', 'NJ', 'NH', 'D', 'L', 'LG', 'LM', 'LB', 'LS', 'LT', 'LP', 'LH', 'M', 'B', 'BS', 'S', 'SS', 'NG', 'J', 'C', 'K', 'T', 'P', 'H'],
}

lookup = {"lead":     ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'],
          "lead_phon":  ['G', 'KK', 'N',  'D', 'TT', 'R', 'M', 'B', 'PP', 'S', 'SS',   '',  'J', 'JJ', 'CH',  'K', 'T', 'P',  'H'],
          "vowel":      ['ㅏ', 'ㅐ', 'ㅑ',  'ㅒ',  'ㅓ',  'ㅔ', 'ㅕ',  'ㅖ', 'ㅗ', 'ㅘ',  'ㅙ',  'ㅚ',  'ㅛ', 'ㅜ', 'ㅝ',  'ㅞ',  'ㅟ',  'ㅠ', 'ㅡ',  'ㅢ', 'ㅣ'],
          "vowel_phon": ['A', 'AE', 'YA', 'YAE', 'EO', 'E', 'YEO', 'YE', 'O', 'WA', 'WAE', 'OE', 'YO', 'U', 'WO', 'WE', 'WI', 'YU', 'EU', 'UI', 'I'],
          "tail":       ['ㄱ', 'ㄲ', 'ᆪ', 'ㄴ', 'ᆬ',  'ᆭ', 'ㄷ', 'ㄹ', 'ᆰ', 'ᆱ', 'ᆲ',  'ᆳ',  'ᆴ', 'ᆵ', 'ᆵ',  'ㅁ', 'ㅂ', 'ᆹ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ᆽ', 'ㅋ','ㅌ', 'ㅍ', 'ㅎ'],
          "tail_phon":  ['K', 'K', 'KS', 'N', 'NJ', 'NH',  'T', 'L', 'LG', 'LM', 'LB', 'LS', 'LT', 'LP', 'LH', 'M', 'P', 'PS', 'T', 'SS', 'NG', 'T',  'T', 'K', 'T', 'P',  'T'],
}




class Symbol:
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.lead = ""
        self.vowel = ""
        self.tail = ""
        self.lead_rom = ""
        self.vowel_rom = ""
        self.tail_rom = ""
        self.is_alpha = True
        if self.symbol.isalpha():
            self.parse()
            self.roman = self.lead_rom+self.vowel_rom+self.tail_rom
        else:
            self.is_alpha = False

    def parse(self) -> None:
        cp = ord(self.symbol) # codepoint
        if 65 <= cp <= 122:
            self.is_alpha = False
            return None
        tail = (cp - 44032) % 28 - 1
        vowel = 1 + int(((cp - 44032 - tail) % 588)/28) - 1
        lead = 1 + int((cp-44032)/588) - 1

        if tail >= 0:
            self.tail = lookup["tail"][tail]
            self.tail_rom = lookup["tail_phon"][tail]

        if vowel >= 0:
            self.vowel = lookup["vowel"][vowel]
            self.vowel_rom = lookup["vowel_phon"][vowel]

        if lead >= 0:
            self.lead = lookup["lead"][lead]
            self.lead_rom = lookup["lead_phon"][lead]

    def pp(self):
        return self.lead+self.vowel+self.tail

    def __repr__(self):
        return self.symbol

class KWord:
    def __init__(self, word: str):
        self.word = word
        self.symbols = []
        self.roman = ""
        self.parse()

    def __repr__(self):
        return self.word

    def parse(self) -> None:
        for symb_in in self.word:
            #print(symb_in)

            symb = Symbol(symb_in)
            self.symbols.append(symb)

        pairs = []
        for symbol in self.symbols:
            if symbol.is_alpha:
                if len(pairs) < 1:
                    pairs.append([symbol])
                elif len(pairs[-1]) < 2:
                    pairs[-1].append(symbol)
                elif len(pairs[-1]) == 2:
                    pairs.append([pairs[-1][1], symbol])
            else:
                if len(pairs) > 0 and len(pairs[-1]) == 2 and pairs[-1][1].is_alpha:
                    pairs.append([pairs[-1][1]])
                pairs.append([symbol])

        if len(pairs) > 0 and len(pairs[-1]) == 2 and pairs[-1][1].is_alpha:
            pairs.append([pairs[-1][1]])

        #pairs = [self.symbols[i:i+2] for i in range(0, len(self.symbols))]
        rom = []
        prev_prov = False
        for pair in pairs:
            prov = ""
            if len(pair) == 2:
                if not prev_prov:
                    rom.append(pair[0].lead_rom + pair[0].vowel_rom)
                else:
                    rom.append(pair[0].vowel_rom)
                    prev_prov = False

                if pair[0].tail and pair[1].lead:
                    prev_prov = True
                    if pair[0].tail == "ㅎ":
                        prov = pair[1].lead_rom
                    else:
                        prov = get_provision(pair[0].tail, pair[1].lead)
                        if not prov:
                            prov = pair[0].tail_rom + pair[1].lead_rom
                elif pair[0].tail and not pair[1].lead:
                    prov = pair[0].tail_rom
            else:
                if pair[0].is_alpha:
                    if prev_prov:
                        if pair[0].tail:
                            prov = pair[0].vowel_rom + pair[0].tail_rom
                        else:
                            prov = pair[0].vowel_rom
                    else:
                        if pair[0].tail:
                            prov = pair[0].lead_rom + pair[0].vowel_rom + pair[0].tail_rom
                        else:
                            prov = pair[0].lead_rom + pair[0].vowel_rom
                else:
                    prov = pair[0].symbol
            if prov:
                rom.append(prov)

            # self.roman += symb.roman
            # else:
            #     self.roman += symb_in
        self.roman = "".join(rom).lower()


def kormalize(words: str) -> str:
    out = []
    for word in words.split(" "):
        w = KWord(word)
        #print(w.word)
        #print(w.symbols[0].pp())
        out.append(w.roman.lower())
    return " ".join(out)


if __name__ == "__main__":
    r = kormalize("Do you remember who we used to be?")
    #             gatda
    print(r)
