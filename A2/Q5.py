def columnar_encrypt(text, key):
    cols = len(key)
    rows = (len(text) + cols - 1) // cols
    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    for i, ch in enumerate(text):
        matrix[i // cols][i % cols] = ch
    order = sorted(range(cols), key=lambda x: key[x])
    result = ''
    for col in order:
        for row in matrix:
            if row[col]:
                result += row[col]
    return result

print(columnar_encrypt("the tomato is a plant in the nightshade family".replace(" ",""),"tomato"))
