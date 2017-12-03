
i = 0

F_xml = open('donnees.txt',encoding = 'utf-8')

ligne = F_xml.readline()

while i < 500001 : # indique la fin du fichier
    
    F_txt = open('page4/'+str(i)+'.txt', 'w',encoding = 'utf-8')
    
    while not('</text' in ligne) :
        F_txt.write(ligne)
        ligne = F_xml.readline()
                    
    F_txt.write(ligne)
    F_txt.close()
    i += 1
    ligne = F_xml.readline()
    
F_xml.close()
