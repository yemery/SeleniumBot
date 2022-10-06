# f=open('Data.py','w+')
# oldArr=['Mme. BOUZARZAR', 'Mme. BOUZARZAR', 'Mme. BOUZARZAR', 'Mme. BENTALEB', 'M. YAHYAOUI', 'M. MOUSTAID', 'M. MOUSTAID', 'M. EL AISSAOUI', 'M. RHANDARI', 'M. MOUSTAID', 'M. MOUATASSIM']
# for i in oldArr:
#     f.writelines(f'"{i}"\n')
f=open("Data.py",'r+')
oldArr=['Mme. BENTALEB', 'Mme. BOUZARZAR', 'Mme. BOUZARZAR', 'Mme. BENTALEB', 'M. YAHYAOUI', 'M. MOUSTAID', 'M. MOUSTAID', 'M. EL AISSAOUI', 'M. RHANDARI', 'M. MOUSTAID', 'M. MOUATASSIM']
lines=f.readlines()
# for line in lines:
#     for i in oldArr:
# bool=True
# for line in range(0,len(lines)):
#     for i in range(0,len(oldArr)):
#         if(i==line):
#             if(lines[line]!=oldArr[i]):
#                 bool=False
#                 break
# print(bool)
# if(bool==False):
#     r=open('Data.py','w+')
#     for i in oldArr:
#         r.writelines(f'"{i}"\n')                
for i in lines:
    print(i)
        
    

