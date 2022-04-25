open("Galatasaray.txt",'w',encoding='UTF-8')
open("Fenerbahce.txt",'w',encoding='UTF-8')
open("Besiktas.txt",'w',encoding='UTF-8')
with open("futbolcu.txt",'r' , encoding='UTF-8') as futbolcular :
    fenerbahceliler = []
    besiktaslılar = []
    galatasaraylılar = []
    okuma = futbolcular.readlines()
    for i in okuma :
        default = i.split(',')
        if default[1]=='Fenerbahçe\n'or default[1]=='Fenerbahçe':
            fenerbahceliler.append(default[0])
        elif default[1]=='Galatasaray\n'or default[1]=='Galatasaray':
            galatasaraylılar.append(default[0])
        elif default[1]=='Beşiktaş\n'or default[1]=='Beşiktaş\n':
            besiktaslılar.append(default[0])
        else :
            print('hata oluştu')
    print(fenerbahceliler)
    print(galatasaraylılar)
    print(besiktaslılar)
with open("Besiktas.txt", 'a', encoding='UTF-8')as besiktas:
    for i in besiktaslılar :
        besiktas.write(i+'\n')
with open("Fenerbahce.txt",'a',encoding='UTF-8')as fenerbahce :
    for i in fenerbahceliler :
        fenerbahce.write(i+'\n')
with open("Galatasaray.txt",'a',encoding='UTF-8')as galatasaray :
    for i in galatasaraylılar :
        galatasaray.write(i+'\n')


