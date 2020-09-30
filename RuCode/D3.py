def intersection(ax1,ay1,ax2,ay2,bx1,by1,bx2,by2):
    #print(ax1,ay1,ax2,ay2,bx1,by1,bx2,by2)
    v1 = (bx2-bx1)*(ay1-by1)-(by2-by1)*(ax1-bx1)
    v2 = (bx2-bx1)*(ay2-by1)-(by2-by1)*(ax2-bx1)
    v3 = (ax2-ax1)*(by1-ay1)-(ay2-ay1)*(bx1-ax1)
    v4 = (ax2-ax1)*(by2-ay1)-(ay2-ay1)*(bx2-ax1)

    return v1*v2 <= 0 and v3*v4 <= 0

a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

print("YES" if intersection(*a,*b) else "NO")
