import matplotlib.pyplot as plt

def printgraph(l):
    sub = l[0] #과목명
    dist = l[1] #분포 리스트

    #x값 설정
    x = []
    for i in dist:
        x.append(i[0])

    #male값 설정
    male = []
    for i in dist:
        male.append(i[1])

    #female값 설정
    female = []
    for i in dist:
        female.append(i[2])

    plt.rcParams['font.family'] ='Malgun Gothic'
    plt.rcParams['axes.unicode_minus'] = False
    plt.scatter(x, male, color = 'blue', label = '남')
    plt.scatter(x, female, color = 'red', label = '여')
    plt.title(f'{l[2]}학년도 수능 {sub}과목 분포')
    plt.legend(loc = 'upper left')
    plt.show()
