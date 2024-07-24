n = int(input())
grades = []
ChineseAndSum = {}
for i in range(n):
    g = input().split()
    # 把各科成绩变成一个列表中的列表
    grade = [int(i) for i in g]
    grades.append(grade)
    # 以编号作为key，value是总分和语文分数的长度为2的列表
    ChineseAndSum[i+1] = [sum(grades[i]),grades[i][0]]

# 给字典排序，第一规则是总分，第二规则是语文分数，第三规则是编号
result = sorted(ChineseAndSum.items(), key = lambda x:[-x[1][0],-x[1][1],x[0]])

# 输出前5名
for i in range(5):
    print(str(result[i][0])+" "+str(result[i][1][0]))