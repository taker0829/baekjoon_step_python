origin_001, origin_002 = input().split()

cvt_001 = int(origin_001[::-1])
cvt_002 = int(origin_002[::-1])

if cvt_001 > cvt_002:
    print(cvt_001)
else:
    print(cvt_002)