def length(a):
    return (a[0]**2 + a[1]**2)**0.5

def scalar(a,b):
    return a[0]*b[0]+a[1]*b[1]

def cross(a,b):
    return b[0]*a[1]-a[0]*b[1]

def get_vector(x1,y1,x2,y2):
    return (x2-x1,y2-y1)

x,y,x1,y1,x2,y2 = [int(i) for i in input().split()]

ao = get_vector(x1,y1,x,y)
ab = get_vector(x1,y1,x2,y2)
bo = get_vector(x2,y2,x,y)
ba = get_vector(x2,y2,x1,y1)
oa = get_vector(x,y,x1,y1)
ob = get_vector(x,y,x2,y2)

if scalar(ao,ab) < 0:
    print(max(length(ao),length(bo)))
elif scalar(bo,ba) < 0:
    print(max(length(ao), length(bo)))
else:
    print(abs(cross(oa,ob)/length(ab)))



