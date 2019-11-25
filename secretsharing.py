import numpy as np
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial

def evaluate_polynomial(p,x):
    deg = len(p)-1
    if deg == 0:
        return p[0]
    return p[0]*(x**deg) + evaluate_polynomial(p[1:],x)

def interpolate(points):
    x, y = np.array([point[0] for point in points]), np.array([point[1] for point in points])
    polynomial = lagrange(x,y)
    return Polynomial(polynomial).coef.tolist()

def expected_result(students_polynomials,a,b):
    deg = len(students_polynomials[0])-1
    expected = 0
    for student in students_polynomials:
        assert len(student) == deg+1, "Incorrect degree polynomial" + student
        expected += evaluate_polynomial(student, 0)
    print("Expected Result:",expected)
    if a == b:
        print("Summing X_i's is valid.")
    else:
        print("Summing X_i's is not valid.")

def secure_sum_with_summing_xi(students_polynomials):
    deg = len(students_polynomials[0])-1
    admins = []
    for j in range(deg+1):
        s = 0
        for student in students_polynomials:
            s += evaluate_polynomial(student,j+1)
        admins.append([(j+1)*(deg+1),s])
    sum_polynomial = interpolate(admins)
    print("Sum Polynomial with summing X_i's",sum_polynomial)
    result = evaluate_polynomial(sum_polynomial, 0)
    print("Result of Secret Sharing Scheme with summing X_i's:", result)
    return result

def secure_sum_without_summing_xi(students_polynomials):
    deg = len(students_polynomials[0])-1
    admins = []
    for j in range(deg+1):
        s = 0
        for student in students_polynomials:
            s += evaluate_polynomial(student,j+1)
        admins.append([j+1,s])
    sum_polynomial = interpolate(admins)
    print("Sum Polynomial without summing X_i's",sum_polynomial)
    result = evaluate_polynomial(sum_polynomial, 0)
    print("Result of Secret Sharing Scheme without summing X_i's:", result)
    return result

inp = [[2,3,5],[3,4,8],[51,6,2],[4,1,2],[90,12,53]]
a = secure_sum_with_summing_xi(inp)
b = secure_sum_without_summing_xi(inp)
expected_result(inp,a,b)

