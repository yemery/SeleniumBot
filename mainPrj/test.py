import numpy as np
wf=open("mainPrj/Data2.txt","r+")
lines=wf.readlines()
arr=[
['M. YAHYAOUI', '#428BCA'] ,
['M. YAHYAOUI', '#428BCA'] ,
['Mme. BOUZARZAR', '#428BCA'] ,
['Mme. BENTALEB', '#428BCA'] ,
['M. YAHYAOUI', '#428BCA'] ,
['M. MOUSTAID', '#428BCA'] ,
['M. MOUSTAID', '#428BCA'] ,
['M. EL AISSAOUI', '#428BCA'] ,
['M. RHANDARI', '#428BCA'] ,
['M. MOUSTAID', '#428BCA'] ,
['M. MOUATASSIM', '#FFFFFF'] ,
]
semiArr=[]
for i in range(0,len(lines)):
    # print(lines[i].rstrip().split(','),'*')
    semiArr.append(lines[i].rstrip().split(','))

# print(semiArr)
npArr=np.array(semiArr)
npArr1=np.array(arr)
print(len(npArr1),len(npArr))
# print(npArr,'******')
# print(npArr1)
# print(np.array_equal(npArr,npArr1))
# print(arr[0])
# print(",".join(arr[0]))
# for j in range(0,len(semiArr)):
#     for k in range(0,len(arr)):
#         if(j==k):
#             # print(semiArr[i],arr[k],'*')
#             print(semiArr[j],arr[k])

#             break
for i in npArr1:
    joinArr=",".join(i)
    print(joinArr)

rf=open("mainPrj/Data2.txt",'w+')
for i in npArr1:
    # print(i)
    joinArr=",".join(i)
    rf.writelines(f'{joinArr}\n')
rf.close()
    
