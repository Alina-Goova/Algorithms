print('Все эл-ты выражения вводите через пробел!')
print('Числа от 1000 до 1999 записывать как "одна тысяча ... "')
def calc(s1):
    zn={'минус':'-', 'плюс':'+', 'умножить':'*', 'делить':'/'}
    ch={"ноль" : 0,
        "один" : 1,
        "два" : 2,
        "три" : 3,
        "четыре" : 4,
        "пять" : 5,
        "шесть" : 6,
        "семь" : 7,
        "восемь" : 8,
        "девять" : 9,
        "десять" : 10,
        "одиннадцать" : 11,
        "двенадцать" : 12,
        "тринадцать" : 13,
        "четырнадцать" : 14,
        "пятнадцать" : 15,
        "шестнадцать" : 16,
        "семнадцать" : 17,
        "восемнадцать" : 18,
        "девятнадцать" : 19,
        "двадцать" : 20,
        "тридцать" : 30,
        "сорок" : 40,
        "пятьдесят" : 50,
        "шестьдесят" : 60,
        "семьдесят" : 70,
        "восемьдесят" : 80,
        "девяносто" : 90,
        'сто' : 100,
        'двести' : 200,
        'триста' : 300,
        'четыреста' : 400,
        'пятьсот' : 500,
        'шестьсот' : 600,
        'семьсот' : 700,
        'восемьсот' : 800,
        'девятьсот' : 900,
        'одна_тысяча' : 1000,
        'две_тысячи' : 2000,
        'три_тысячи' : 3000,
        'четыре_тысячи' : 4000,
        'пять_тысяч' : 5000,
        'шесть_тысяч' : 6000,
        'семь_тысяч' : 7000,
        'восемь_тысяч' : 8000,
        'девять_тысяч' : 9000}

    s1=' '+s1
    mark=0
    if ' тысяч' in s1:
        s1=s1.replace(' тысяч', '_тысяч')
    s=s1.split() #выражение

    k=0
    list1=[]
    for i in s:
        if i=='на' or i=='скобка':
            continue
        if i in ch and k==1:
            list1[-1]+=' '+i
            continue
        if i=='открывается':
            list1.append('(')
            continue
        elif i=='закрывается':
            list1.append(')')
            continue
        elif i in ch:
            k=1
        else:
            k=0
        if 'делить' in i:
            list1.append('делить')
        else:
            list1.append(i)
    list2=[]*len(list1)

    summ=0
    znak=''
    for i in list1:
        qq=i.split(' ')
        for j in qq:
            if j in ch:
                summ+=ch[j]
            elif j in zn:
                znak=zn[j]
        if znak!='':
            list2.append(znak)
        elif i=='(' or i==')':
            list2.append(i)
        else:
            list2.append(str(summ))
        summ=0
        znak=''
    for i in list2:
        znak+=i
    znak=str(eval(znak))
    otv=''
    m=-1
    for i in znak:
        if i in '0123456789':
            m+=1
    for i in znak:
        if not(i in '0123456789'):
            continue
        for j in ch:
            if ch[j]==int(i)*(10**m):
                otv+=j+' '
        m-=1
    if znak[0]=='-':
        otv='минус '+otv
    print('-->', otv)
calc(input().lower())
