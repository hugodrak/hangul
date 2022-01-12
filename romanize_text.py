from normalize_kor import kormalize
from translate_google import translate_text
words = []
out = open('y2y_r.txt', 'w')
with open('year2year.txt', 'r') as f:
    lines = f.read().splitlines()

    for row in lines:
        out.write(" - ".join([row, kormalize(row), translate_text(row)])+"\n")
