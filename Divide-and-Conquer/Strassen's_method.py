"""Module used for implementing strassen's method"""


# helper function: adds two matrices together
def add(A, B):
    n = len(A)
    # This creates a new grid, adding each matching cell
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]


# helper function: subtracts two matrices
def sub(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]



def strassen(A, B): #takes O(n^(2.8)) time
    n = len(A)

    # BASE CASE: If the matrix is just a 1x1
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    # DIVIDE STEP: Find the middle line to slice the grids into quarters
    mid = n // 2

    # slicing matrix A into 4 quarters (a, b, c, d)
    a = [[A[i][j] for j in range(mid)] for i in range(mid)]  # Top-Left
    b = [[A[i][j] for j in range(mid, n)] for i in range(mid)]  # Top-Right
    c = [[A[i][j] for j in range(mid)] for i in range(mid, n)]  # Bottom-Left
    d = [[A[i][j] for j in range(mid, n)] for i in range(mid, n)]  # Bottom-Right

    # slicing matrix B into 4 quarters (e, f, g, h)
    e = [[B[i][j] for j in range(mid)] for i in range(mid)]  # Top-Left
    f = [[B[i][j] for j in range(mid, n)] for i in range(mid)]  # Top-Right
    g = [[B[i][j] for j in range(mid)] for i in range(mid, n)]  # Bottom-Left
    h = [[B[i][j] for j in range(mid, n)] for i in range(mid, n)]  # Bottom-Right

    # conquer:Strassen formulas
    p1 = strassen(a, sub(f, h))  # p1 = a(f - h)
    p2 = strassen(add(a, b), h)  # p2 = (a + b)h
    p3 = strassen(add(c, d), e)  # p3 = (c + d)e
    p4 = strassen(d, sub(g, e))  # p4 = d(g - e)
    p5 = strassen(add(a, d), add(e, h))  # p5 = (a + d)(e + h)
    p6 = strassen(sub(b, d), add(g, h))  # p6 = (b - d)(g + h)
    p7 = strassen(sub(a, c), add(e, f))  # p7 = (a - c)(e + f)

    # combine
    c11 = add(sub(add(p5, p4), p2), p6)  # c11 = p5 + p4 - p2 + p6
    c12 = add(p1, p2)  # c12 = p1 + p2
    c21 = add(p3, p4)  # c21 = p3 + p4
    c22 = sub(sub(add(p1, p5), p3), p7)  # c22 = p1 + p5 - p3 - p7

    # reassemble the four quarters back into one giant grid
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(mid):
        for j in range(mid):
            C[i][j] = c11[i][j]  # Top-left corner
            C[i][j + mid] = c12[i][j]  # Top-right corner
            C[i + mid][j] = c21[i][j]  # Bottom-left corner
            C[i + mid][j + mid] = c22[i][j]  # Bottom-right corner

    return C


if __name__ == "__main__":
    A = [
        [1, 2],
        [3, 4]
    ]
    B = [
        [5, 6],
        [7, 8]
    ]

    Result = strassen(A, B)
    print("Strassen Result")
    for row in Result:
        print(row)
