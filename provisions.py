
rows = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅅ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅌ', 'ㅎ']
cols = ['ㅇ', 'ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅅ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

mat_2 = [
['g', 'kg', 'ngn', 'kd', 'ngn', 'ngm', 'kb', 'ks', 'kj', 'kch', 'k-k', 'kt', 'kp', 'kh, k'],
['n', 'n-g', 'nn', 'nd', 'll, nn', 'nm', 'nb', 'ns', 'nj', 'nch', 'nk', 'nt', 'np', 'nh'],
['d, j', 'tg', 'nn', 'td', 'nn', 'nm', 'tb', 'ts', 'tj', 'tch', 'tk', 't-t', 'tp', 'th, t, ch'],
['r', 'lg', 'll, nn', 'ld', 'll', 'lm', 'lb', 'ls', 'lj', 'lch', 'lk', 'lt', 'lp', 'lh'],
['m', 'mg', 'mn', 'md', 'mn', 'mm', 'mb', 'ms', 'mj', 'mch', 'mk', 'mt', 'mp', 'mh'],
['b', 'pg', 'mn', 'pd', 'mn', 'mm', 'pb', 'ps', 'pj', 'pch', 'pk', 'pt', 'p-p', 'ph, p'],
['s', 'tg', 'nn', 'td', 'nn', 'nm', 'tb', 'ts', 'tj', 'tch', 'tk', 't-t', 'tp', 'th, t, ch'],
['ng-', 'ngg', 'ngn', 'ngd', 'ngn', 'ngm', 'ngb', 'ngs', 'ngj', 'ngch', 'ngk', 'ngt', 'ngp', 'ngh'],
['j', 'tg', 'nn', 'td', 'nn', 'nm', 'tb', 'ts', 'tj', 'tch', 'tk', 't-t', 'tp', 'th, t, ch'],
['ch', 'tg', 'nn', 'td', 'nn', 'nm', 'tb', 'ts', 'tj', 'tch', 'tk', 't-t', 'tp', 'th, t, ch'],
['t, ch', 'tg', 'nn', 'td', 'nn', 'nm', 'tb', 'ts', 'tj', 'tch', 'tk', 't-t', 'tp', 'th, t, ch'],
['h', 'k', 'nn', 't', 'nn', 'nm', 'p', 'hs', 'ch', 'tch', 'tk', 't', 'tp', 't']]

mat = [
['g', 'kg', 'ngn', 'kd', 'ngn', 'ngm', 'kb', 'ks', 'kj', 'kch', 'kk', 'kt', 'kp', 'k'],
['n', 'ng', 'nn', 'nd', 'll', 'nm', 'nb', 'ns', 'nj', 'nch', 'nk', 'nt', 'np', 'nh'],
['d', 'tg', 'nn', 'td', 'nn', 'nm', 'tb', 'ts', 'tj', 'tch', 'tk', 'tt', 'tp', 'th'], # 'th, t, ch'
['r', 'lg', 'll, nn', 'ld', 'll', 'lm', 'lb', 'ls', 'lj', 'lch', 'lk', 'lt', 'lp', 'lh'],
['m', 'mg', 'mn', 'md', 'mn', 'mm', 'mb', 'ms', 'mj', 'mch', 'mk', 'mt', 'mp', 'mh'],
['b', 'pg', 'mn', 'pd', 'mn', 'mm', 'pb', 'ps', 'pj', 'pch', 'pk', 'pt', 'pp', 'ph, p'],
['s', 'tg', 'nn', 'td', 'nn', 'nm', 'tb', 'ts', 'tj', 'tch', 'tk', 'tt', 'tp', 'th'],
['ng', 'ngg', 'ngn', 'ngd', 'ngn', 'ngm', 'ngb', 'ngs', 'ngj', 'ngch', 'ngk', 'ngt', 'ngp', 'ngh'],
['j', 'tg', 'nn', 'td', 'nn', 'nm', 'tb', 'ts', 'tj', 'tch', 'tk', 'tt', 'tp', 'th'],
['ch', 'tg', 'nn', 'td', 'nn', 'nm', 'tb', 'ts', 'tj', 'tch', 'tk', 'tt', 'tp', 'th'],
['t', 'tg', 'nn', 'td', 'nn', 'nm', 'tb', 'ts', 'tj', 'tch', 'tk', 'tt', 'tp', 'th'],
['h', 'k', 'nn', 't', 'nn', 'nm', 'p', 'hs', 'ch', 'tch', 'tk', 't', 'tp', 't']]


def get_provision(first, second):
    if first in rows and second in cols:
        i1 = rows.index(first)
        i2 = cols.index(second)
        if i1 is not None and i2 is not None:
            return mat[i1][i2]