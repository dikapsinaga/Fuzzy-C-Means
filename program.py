import numpy as np

def cartesianProduct(x,y):
    # np.ravel untuk meratakan aray
    # np.asarray memastikan dalam bentuk array

    x = np.asarray(x).ravel()
    y = np.asarray(y).ravel()


    m, n = len(x), len(y)

    # at least_2d merubah array yg masuk menjadi 2d dan .T artinya ditransformasi e.g 1*3 jadi 3*1
    # np.ones membuat aray, eg np.ones((1,n)) -> [1, 1, 1]
    # np.matmul membuat perkalian matriks

    a = np.matmul(np.atleast_2d(x).T, np.ones((1, n)))
    b = np.matmul(np.ones((m, 1)), np.atleast_2d(y))

    # np.fmin mencari setiap i,j nilai minimalnya

    return np.fmin(a, b)

def maxMinComposition(s,r):

    # memastikan s dan r adalah array
    s = np.asarray(s)
    r = np.asarray(r)

    if s.ndim < 2:
        s = np.atleast_2d(s)
    if r.ndim < 2:
        r = np.atleast_2d(r).T

    # untuk membuat array kosongan. Dimensi sesuai dengan hasilnya
    m = s.shape[0]
    p = r.shape[1]
    t = np.zeros((m, p))

    # mengisi nilai array kosongan menggunakan maxmincomposition
    for pp in range(p):
        for mm in range(m):
            t[mm, pp] = (np.fmin(s[mm, :], r[:, pp].T)).max()
    return t

def maxProduct(s,r ):
    s = np.asarray(s)
    r = np.asarray(r)


    if s.ndim < 2:
        s = np.atleast_2d(s)
    if r.ndim < 2:
        r = np.atleast_2d(r).T

    m = s.shape[0]
    p = r.shape[1]
    t = np.zeros((m, p))

    for mm in range(m):
        for pp in range(p):
            t[mm, pp] = (s[mm, :] * r[:, pp].T).max()

    return t

x = []
y = []
z = []

for i in range(0,6):
    print("Input X",i,": ",end="")
    temp = float(input())
    x.append(temp)


for i in range(0,6):
    print("Input Y",i, ": ",end="")
    temp = float(input())
    y.append(temp)

print("")

for i in range(0,6):
    print("Input Z",i, ": ",end="")
    temp = float(input())
    z.append(temp)

print("\nX (bandwith) = ", x)
print("Y (latency) = ", y)
print("X' (new bandwith) = ", z)

R = cartesianProduct(x, y)
print("\nRelasi X to Y : ")
print(R)

a = np.atleast_2d(x).T
print(a)


newY = maxMinComposition(z, R)
print("\nY' (new Latency) = ", newY)

newMaxProd = maxProduct(z, R)
print("\nMax Product : ", newMaxProd)

