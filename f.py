import matplotlib.pyplot as plt
import numpy as np
ns = []
matches = []
comps = []
with open('t.txt', 'r') as f:
    for line in f.read().splitlines():
        s = line.split(' ')
        ns.append(int(s[0]))
        matches.append(int(s[1]))
        comps.append(int(s[2]))

log = [np.log2(x) for x in ns]
nlog = [x*np.log2(x) for x in matches]
plt.plot(ns, matches)
plt.plot(ns, comps)
plt.plot(ns, log)
plt.plot(ns, nlog)
# plt.legend(['comps', 'log(n)'])#, 'log(n)', 'log(n) + m*log(m)'])
plt.legend(['matches','comps', 'log(n)', 'mlogm'])
plt.show()
