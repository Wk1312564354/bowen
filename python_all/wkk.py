# a = [20, 25, 17, 37, 5]
# b = []
# for i in range(len(a)-1):
#     m = min(a)
#     b.append(m)
#     a.remove(m)
# a = b
# print(a)

# import mokuai
# mokuai.wk()
# mokuai.wkk()

# b = 0
# for i in range(1,1000):
#     a = str(i).count("3")
#     b += a
# print(b)
#
# k = {"a": "nihao", "b": {"c": "12","e": "abc"}}
# k.pop("b")
# print(k)

import re
a = "a123aa456aa"
b = re.findall(re.compile('a(.*?)a',re.S),a)
print(b)
