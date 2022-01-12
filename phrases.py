from normalize_kor import kormalize
phrases = []

out = open("comp.txt", "w")

with open("phrases.txt", "r") as f:
    for line in f.read().splitlines():
        sp = line.split("\t")
        nl = [x.lstrip() for x in sp]
        if len(nl) > 2:
            kword = kormalize(nl[1])
            if nl[2] != kword:
                out.write("\t\t".join([nl[1], nl[2], kword.lower()])+"\n")
out.close()