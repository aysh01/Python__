# a=[23,23,23,123,123,111]
# print(a)
# a.sort()
# print(a)

a=[23,123,14,134,'abc']
a[1:3]=['abc',1000]
# print(a)
for i,j in enumerate(a):
    if i == 1:
        pass
    elif j == a[3]:
        pass
    else:
        print('The, value at index ',i,' is: ',j)
        # break

