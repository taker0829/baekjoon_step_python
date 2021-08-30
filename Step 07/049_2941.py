croatia_str = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
ipt_str = input()

for str_part in croatia_str:
    ipt_str = ipt_str.replace(str_part, '*')

#print(ipt_str)
print(len(ipt_str))