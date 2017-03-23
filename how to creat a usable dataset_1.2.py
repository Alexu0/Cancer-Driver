#for cycle2 
ff=open("/Users/apple/Desktop/domainXplorer-master/example_files/cycle 2/for_matlab_anlyze.txt")
fr=open("/Users/apple/Desktop/domainXplorer-master/example_files/cycle 2/for_matlab_anlyze_cycle_2.txt","w")
f=open("/Users/apple/Desktop/domainXplorer-master/example_files/cycle 2/missense_mutations_TCGA_ramian_1.txt")
ms=f.read()
ms=ms.split("\n")
f.close()
dicn=ff.readline()
fr.write(dicn)
dicn=dicn.split(" ")
tl=ff.readline()

q=" "
x=1
z=1
while tl!="":
        tlsp=tl.split(" ")
        for i in ms:
                isp=i.split("\t")
                if isp[0]==tlsp[0]:
                        for j in range(len(dicn)):
                                if j>1 and dicn[j].split("\t")[0]==isp[1] and isp[2]>=dicn[j].split("\t")[1].split("-")[1] and isp[2]<=dicn[j].split("\t")[1].split("-")[2]:
                                        tlsp[j]="1"
                                        tl=q.join(tlsp)
                                        ms.remove(i)
                                        if z%1000==0:
                                                print("this is "+str(z)+" ms")
                                        z+=1
                                        break
        fr.write(tl)
        tl=""
        tl=ff.readline()
        print(x)
        x+=1

ff.close()
fr.close()

#ms[0:4]
#['TCGA-OR-A5JU\tENSP00000342313\t343', 'TCGA-PK-A5HB\tENSP00000342313\t343', 'TCGA-OR-A5JB\tENSP00000342313\t343', 'TCGA-OR-A5JP\tENSP00000368644\t197']
#tl.split(" ")[0:4]
#['TCGA-06-0644', '842.67613', '0', '0']
#dicn[0:4]
#['name', 'score', 'ENSP00000337816\tIDR-90-129', 'ENSP00000337816\tPF00045-416-457']
