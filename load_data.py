from normalize_kor import kormalize
words = []
out = open('new_dataset.txt', 'w')
with open('dataset_words.txt', 'r') as f:
    lines = f.read().splitlines()
    splitted = [lines[i:i+6] for i in range(0, len(lines), 6)]
    for row in splitted:

        hang = row[2].lstrip()

        word = [row[0], hang, row[4].lstrip(), kormalize(hang), ""]
        out.write("\t".join(word)+"\n")
