#update with higher efficiency 
ff=open("C:/Users/N1604313C/Desktop/test 1.4/for_matlab_anlyze_before.txt")
fr=open("C:/Users/N1604313C/Desktop/test 1.4/for_matlab_anlyze.txt","w")
f=open("C:/Users/N1604313C/Desktop/test 1.4/missense_mutations_TCGA.txt")
ms=f.read()
ms=ms.split("\n")
f.close()
matrix=ff.read()
print("reading finished")
matrix=matrix.split("\n")
dicn=matrix[0]
#dicn=ff.readline()
#fr.write(dicn)
dicn=dicn.split(" ")
#tl=ff.readline()

q=" "
x=1
z=1
pe=len(dicn)
re=len(ms)
#while tl!="":
for tln in range(len(matrix)):
        if tln==0:
                continue
        tl=matrix[tln]
        tlsp=tl.split(" ")
        for i in ms:
                isp=i.split("\t")
                if isp[0]==tlsp[0] and isp!=[""]:
                        for j in range(len(dicn)):
                                if j>1 :#and dicn[j].split("\t")[0]==isp[1] and int(isp[2])>=int(dicn[j].split("\t")[1].split("-")[1]) and int(isp[2])<=int(dicn[j].split("\t")[1].split("-")[2]):
                                        if dicn[j].split("\t")[0]==isp[1]:
                                                if int(isp[2])>=int(dicn[j].split("\t")[1].split("-")[1]) and int(isp[2])<=int(dicn[j].split("\t")[1].split("-")[2]):
                                                        tlsp[j]="1"
                                                        tl=q.join(tlsp)
                                                        if z%(re/100)==0:
                                                                print("this is "+str(z/(re/100))+" ms")
                                                        z+=1
                                                        break
                                                    
                                        #tlsp[j]="1"
                                        #tl=q.join(tlsp)
                                        #ms.remove(i)
                                        #if z%(re/100)==0:
                                                #print("this is "+str(z/(re/100))+" ms")
                                        #z+=1
                                        #break
        #fr.write(tl)
        matrix[tln]=tl
        del tl
        #tl=""
        #tl=ff.readline()
        #print(x)
        #x+=1

matrix="\n".join(matrix)
fr.write(matrix)
ff.close()
fr.close()

#ms[0:4]
#['TCGA-OR-A5JU\tENSP00000342313\t343', 'TCGA-PK-A5HB\tENSP00000342313\t343', 'TCGA-OR-A5JB\tENSP00000342313\t343', 'TCGA-OR-A5JP\tENSP00000368644\t197']
#tl.split(" ")[0:4]
#['TCGA-06-0644', '842.67613', '0', '0']
#dicn[0:4]
#['name', 'score', 'ENSP00000337816\tIDR-90-129', 'ENSP00000337816\tPF00045-416-457']
