def diffie_hellman(p, g, a, b):
    A = pow(g, a, p)
    B = pow(g, b, p)
    shared_a = pow(B, a, p)
    shared_b = pow(A, b, p)
    return shared_a, shared_b

print(diffie_hellman(11,7,3,6))
