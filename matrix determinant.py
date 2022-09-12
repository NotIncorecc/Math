m = [ [7,2,3,24],[11,5,76,21],[14,8,4,7],[8,11,12,23]]

def p2(matrix):
    return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

def give_minor(matrix, indexofelement_infirstrow):
    n = matrix.copy()
    n.pop(0)
    ne = []
    for i in n:
        l = i.copy()
        l.pop(indexofelement_infirstrow)
        ne.append(l)
    return ne


def pn(matrix):
    a=0
    c  = 1
    h= matrix[0]
    for i in range(0,len(h)):
        a+= c* h[i] * p2(give_minor(matrix,i))
        c=c*-1
    
    return a

def funcher(func):
    def funched(matrix):
        a=0
        h=matrix[0]
        for i in range(0,len(h)):
            a += (-1)**i * h[i] * func(give_minor(matrix,i))
        return a
    return funched

j = len(m)
if j ==1:
    print(m[0][0])
elif j==2:
    print(p2(m))
elif j==3:
    print(pn(m))
elif j>=4:
    for i in range(1,j-2):
        pn = funcher(pn)
    print(pn(m))
