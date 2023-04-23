from django.shortcuts import render

import math

# Create your views here.

def layout(request): 
    return render(request, 'Maths_Equations/layout.html')

def ansbook(request): 
    value1 = request.GET['first']
    value2 = request.GET['second']
    total = int(value1) + int(value2)
    return render(request, 'Maths_Equations/ansbook.html', {
        'ans': ('%.2f' % total)
    })


def ansbook1(request): 
    value1 = request.GET['first']
    value2 = request.GET['second']
    total = int(value1) - int(value2)
    return render(request, 'Maths_Equations/ansbook.html', {
        'ans': ('%.2f' % total)
    })


def ansbook3(request): 
    value1 = request.GET['first']
    value2 = request.GET['second']
    total = int(value1) * int(value2)
    return render(request, 'Maths_Equations/ansbook.html', {
        'ans': ('%.2f' % total)
    })


def ansbook4(request): 
    value1 = request.GET['first']
    total = int(value1) * int(value1)
    return render(request, 'Maths_Equations/ansbook.html', {
        'ans': ('%.2f' % total)
    })


def ansbook5(request): 
    value1 = request.GET['first']
    total = math.sqrt(int(value1))
    return render(request, 'Maths_Equations/ansbook.html', {
        'ans': ('%.2f' % total)
    })


def ansbook2(request): 
    value1 = request.GET['first']
    value2 = request.GET['second']
    total = int(value1) / int(value2)
    return render(request, 'Maths_Equations/ansbook.html', {
        'ans': ('%.2f' % total)
    })


# def area(request):
#     r = request.GET['first']
#     r = int(r)
#     total = 3.142 * (r ** 2)
#     return render(request, 'Maths_Equations/ansbook.html', {
#         'ans' : total
#     })


def ansbook7(request): 
    r = request.GET['first']
    r = int(r)
    total = 3.142 * (r ** 2)
    return render(request, 'Maths_Equations/circle_ansbook.html', {
        'ans': ('%.2f' % total)
    })


def ansbook8(request): 
    r = request.GET['first']
    r = int(r)
    total = 2 * 3.142 * r
    return render(request, 'Maths_Equations/circle_ansbook.html', {
        'ans': ('%.2f' % total)
    })

def varian(request):
    return render(request, 'Maths_Equations/variation.html')


def varians(request): 
    a1 = request.GET['first']
    a1 = int(a1)
    b1 = request.GET['second']
    b1 = int(b1)
    a2 = request.GET['third']
    a2 = int(a2)
    b2 = request.GET['forth']
    b2 = int(b2)
    bin = b1*a2
    bin1 = b2*a1
    if b2 == 0:
        total = bin/a1
        total1 = a1/b1
    elif a1 == 0:
        total = (bin/b2)
        total1 = (a2/b2)
    elif b1 == 0:
        total = (bin1/a2)
        total1 = (a2/b2)
    elif a2 == 0:
        total = (bin1/b1)
        total1 = (a1/b1)
        
    return render(request, 'Maths_Equations/varia_ansbook.html', {
        'ans' : total,
        'ans1' : total1
    })

def quad(request):
    value1 = float(request.GET['first'])
    value2 = float(request.GET['second'])
    value3 = float(request.GET['third'])
    nat1 = value2 * -1
    nat2 = value2**2
    nat3 = (nat2) - (4*value1*value3)
    nat4 = math.sqrt(nat3)
    nat5 = 2*value1
    nat6 = nat1 + nat4
    nat7 = nat1 - nat4
    ans1 = nat6/nat5
    ans2 = nat7/nat5
    return render(request, 'Maths_Equations/quad_ansbook.html', {
        'ans': ('%.2f' % ans1),
        'ans1': ('%.2f' % ans2)
    })
def simul(request):
    value1 = int(request.GET['first'])
    value2 = int(request.GET['second'])
    value3 = int(request.GET['third'])
    value4 = int(request.GET['forth'])
    value5 = int(request.GET['fifth'])
    value6 = int(request.GET['sixth'])
    mult1 = value1*value5
    mult1 = int(mult1)
    mult2 = value4*value2
    mult2 = int(mult2)
    sub = (mult1 - mult2)
    mult12 = value3*value5
    mult22 = value6*value2
    sub2 = (mult12 - mult22)
    mult13 = value1*value6
    mult23 = value4*value3
    sub3 = (mult13 - mult23)
    div = sub2 / sub
    div2 = sub3 / sub
    # total = math.sqrt(int(value1))
    return render(request, 'Maths_Equations/simul_ansbook.html', {
        'ans': ('%.2f' % div),
        'ans1': ('%.2f' % div2)

    })

def addition(request):
    return render(request, 'Maths_Equations/addition.html')

    
def subtraction(request):
    return render(request, 'Maths_Equations/subtraction.html')

    
def division(request):
    return render(request, 'Maths_Equations/division.html')

    
def multiplication(request):
    return render(request, 'Maths_Equations/multiplication.html')

    
def variation(request):
    return render(request, 'Maths_Equations/variation.html')

    
def inverse(request):
    return render(request, 'Maths_Equations/inverse.html')


def inverses(request):
    a1 = request.GET['first']
    a1 = int(a1)
    b1 = request.GET['second']
    b1 = int(b1)
    a2 = request.GET['third']
    a2 = int(a2)
    b2 = request.GET['forth']
    b2 = int(b2)
    k1 = a1*b1
    k2 = a2*b2
    if a2 == 0:
        total = (k1/b2) 
        total1 = (k1)
    if b2 == 0:
        total = (k1/a2)
        total1 = (k1)
    if a1 == 0:
        total = (k2/b1)
        total1 = (k2)
    if b1 == 0:
        total = (k2/a1)
        total1 = (k2)
    return render(request, 'Maths_Equations/varia_ansbook.html', {
        'ans' : total,
        'ans1' : total1
    })

    
def joint(request):
    return render(request, 'Maths_Equations/joint.html')


def joints(request):
    a = int(request.GET['first'])
    b = int(request.GET['second'])
    c = int(request.GET['third'])
    a1 = int(request.GET['forth'])
    b1 = int(request.GET['fifth'])
    c1 = int(request.GET['sixth'])
    if a == 0:
        acc = a1*c1*b
        acc1 = a1 * c1
        total = acc / (c*b1)
        total1 = b1 /acc1
    elif b == 0:
        acc = a * c * b1
        acc1 = a1 * c1
        total = acc / (a1 * c1)
        total = b1 / acc1
    elif c == 0:
        acc = a1 * c1 * b
        acc1 = a1 * c1
        total = acc / (a*b1)
        total1 = b1 / acc1
    elif a1 == 0:
        acc = a * c * b1
        acc1 = a * c
        total = acc / (b * c1)
        total1 = b / acc1
    elif b1 == 0:
        acc = a1 * c1 *b 
        acc1 = a * c
        total = acc / (a * c)
        total1 = b /acc1
    elif c1 == 0:
        acc = a * c * b1
        acc1 = a * c
        total = acc / (b * a1)
        total1 = b /acc1
    return render(request, 'Maths_Equations/varia_ansbook.html', {
        'ans' : total,
        # 'ans1' : total1
    })

    
def partial(request):
    return render(request, 'Maths_Equations/partial.html')

    
def quadratic(request):
    return render(request, 'Maths_Equations/quadratic.html')

    
def matrix(request):
    return render(request, 'Maths_Equations/matrix.html')

def matt(request):
    a = int(request.GET['a'])
    b = int(request.GET['b'])
    a1 = int(request.GET['a1'])
    b1 = int(request.GET['b1'])
    x = int(request.GET['x'])
    y = int(request.GET['y'])
    x1 = int(request.GET['x1'])
    y1 = int(request.GET['y1'])
    X1 = (a*x) + (b*x1)
    Y1 = (a * y) + (b*y1)
    X2 = (a1 * x) + (b1 * x1)
    Y2 = (a1 *y) + (b1 * y1)
    return render(request, 'Maths_Equations/matt.html', {
        'ans1': X1,
        'ans2': Y1,
        'ans3': X2,
        'ans4': Y2,
    })

def sqmatt(request):
    return render(request, 'Maths_Equations/squarematt.html')


def sqmat(request):
    a = int(request.GET['a'])
    b = int(request.GET['b'])
    a1 = int(request.GET['a1'])
    b1 = int(request.GET['b1'])
    X1 = (a*a) + (b*a1)
    Y1 = (a * b) + (b*b1)
    X2 = (a1 * a) + (b1 * a1)
    Y2 = (a1 *b) + (b1 * b1)
    return render(request, 'Maths_Equations/matt.html', {
        'ans1': X1,
        'ans2': Y1,
        'ans3': X2,
        'ans4': Y2,
    })

def dett(request):
    return render(request, 'Maths_Equations/determinant.html')

def det(request):
    a = int(request.GET['a'])
    b = int(request.GET['b'])
    a1 = int(request.GET['a1'])
    b1 = int(request.GET['b1'])
    br1 = a * b1
    br2 = a1 * b
    deter = br1 - br2
    return render(request, 'Maths_Equations/matt.html', {
        "ans" : deter
    } )


def invmatt(request):
    return render(request, 'Maths_Equations/inversematt.html')

def invmat(request):
    a = int(request.GET['a'])
    b = int(request.GET['b'])
    a1 = int(request.GET['a1'])
    b1 = int(request.GET['b1'])
    X1 = b1
    Y1 = -b
    X2 = -a1
    Y2 = a
    return render(request, 'Maths_Equations/matt.html', {
        'ans1': X1,
        'ans2': Y1,
        'ans3': X2,
        'ans4': Y2,
    })
    
def simultaneous(request):
    return render(request, 'Maths_Equations/simultaneous.html')

    
def calculus(request):
    return render(request, 'Maths_Equations/calculus.html')

    
def circle(request):
    return render(request, 'Maths_Equations/circle.html')


    
def polygon(request):
    return render(request, 'Maths_Equations/polygon.html')

    
def square_root(request):
    return render(request, 'Maths_Equations/square_root.html')

    
def square(request):
    return render(request, 'Maths_Equations/square.html')

    
def area(request):

    return render(request, 'Maths_Equations/area.html')

    
def perimeter(request):
    return render(request, 'Maths_Equations/perimeter.html')

    