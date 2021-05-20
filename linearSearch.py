path1 = 'ResultK.txt'
path2 = 'result_data.txt'

text1 = [ele for ele in open(path1,'r', encoding="utf8")]
text2 = [ele for ele in open(path2,'r', encoding="utf8")]

print(len(text1), len(text2))
for i in range(0, len(text2)):
    if(text2[i]!=text1[i]):
        print(i, text1[i], text2[i])
        break