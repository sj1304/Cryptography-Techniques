def generate_matrix(key):

    key = "".join(sorted(set(key.upper()), key=lambda x: key.upper().index(x)))
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  
    used = set()
    matrix = []
    for ch in key + alphabet:
        if ch not in used:
            matrix.append(ch)
            used.add(ch)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j
    raise ValueError(f"Character {ch} not found in matrix")

def playfair_encrypt(text, key):
    matrix = generate_matrix(key)
    text = text.upper().replace("J", "I").replace(" ", "")
    
    # Build pairs
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'X'
        if a == b:  
            b = 'X'
            i += 1
        else:
            i += 2
        pairs.append((a, b))
    

    result = ""
    for a, b in pairs:
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)
        if r1 == r2:  
            result += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
        elif c1 == c2:  
            result += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
        else:  
            result += matrix[r1][c2] + matrix[r2][c1]
    return result

def flow(text, key):
    return playfair_encrypt(text, key)


print("Playfair Encrypt:",flow("I LIKE STRAWBERRIES", "ICECREAM"))
