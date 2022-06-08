#most frequent element#worstmethod
#mrn=14
#frn=11
# lst=[10,11,11,12,13,14,14,14]
# dup_lst=[]
# for i in range(0,len(lst)):
#     for j in range((i+1),len(lst)):
#         if lst[i]==lst[j]:
#             dup_lst.append(lst[i])
#  print(f" 1strecursive element{dup_lst[i]} second recursive element {dup_lst[j]}")

#bestmethod using dictionary

lst=[2,3,4,6,10]

sum=8
# for i in range(len(lst)):
#     for j in range((i+1),len(lst)):
#         cur_sum=lst[i]+lst[j]
#         if cur_sum==sum:
#             print(f"pairs {lst[i], lst[j]}")
#             break

lst.sort()
element=7
low=0
upp=len(lst)-1
while (upp>low):
    cur_sum=lst[low]+lst[upp]
    if element==cur_sum:
        print(f"pairs{lst[upp]},{lst[low]}")
        break
    elif element>cur_sum:
        low+=1
    elif element<cur_sum:
        upp-=1











