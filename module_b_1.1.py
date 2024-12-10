def reader(file): #파일 읽기
    import csv
    f = open(file,'r',newline="")
    rdr = csv.reader(f)
    return rdr

def year_choice():
    year = input('연도 선택(2020,2021,2022,2023) :')
    if year == '2020':
        file = '20201231.csv'
    elif year == '2021':
        file = '20211231.csv'
    elif year == '2022':
        file = '20221231.csv'
    elif year == '2023':
        file = '20231231.csv'
    return file

def subject_name(): #과목 리스트 만들기 + 과목 선택받기
    subject_list = []
    file = year_choice()
    rdr = reader(file)
    for line in rdr:
        if line[0] == '영역':
            continue
        if line[1] not in subject_list:
            subject_list.append(line[1])
    for i in subject_list:
        if i == subject_list[-1]:
            print(i,end=' ')
            break
        print(i,end=',')
    subject_choice = input('중 하나의 과목을 선택해주세요 :')

    return subject_choice, file

def chosen_subject(): #선택된 과목의 리스트 만들기
    chosen_subject_list=[]
    subject_choice,file = subject_name()
    final_list =[]
    final_list.append(subject_choice)
    rdr = reader(file)
    for line in rdr:
        if line[1] == subject_choice:
            line[2] = int(line[2])
            line[3] = int(line[3])
            line[4] = int(line[4])
            chosen_subject_list.append((line[2:5]))
    final_list.append(chosen_subject_list)
    final_list.append(file[0:4])
    return final_list
