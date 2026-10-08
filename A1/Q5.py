r = 5

def matrix(plntxt, key):
    ikey = 0
    i = 0
    j = 0

    m = [['' for _ in range(5)] for _ in range(5)]

    key = ''.join(key.split()).lower()

    for ikey in range(len(key)):
        ch = key[ikey]

        found = False
        for row in m:
            if ch in row:
                found = True
                break

        if not found:
            m[j][i] = ch
            i += 1

            if i == 5:
                i = 0
                j += 1

    chord = 0

    while j < 5:
        ch = chr(ord('a') + chord)

        if ch != 'j':
            found = False
            for row in m:
                if ch in row:
                    found = True
                    break

            if not found:
                m[j][i] = ch
                i += 1

                if i == 5:
                    i = 0
                    j += 1

        chord += 1

    return m


def ciphertxt(plntxt, key):
    m = matrix(plntxt, key)

    plntxt = ''.join(plntxt.split()).lower()
    plntxt = plntxt.replace('j', 'i')

    pairs = []
    i = 0

    while i < len(plntxt):
        a = plntxt[i]

        if i + 1 < len(plntxt):
            b = plntxt[i + 1]

            if a == b:
                pairs.append(a + 'x')
                i += 1
            else:
                pairs.append(a + b)
                i += 2
        else:
            pairs.append(a + 'x')
            i += 1

    cipher = ""

    for pair in pairs:
        a = pair[0]
        b = pair[1]

        r1 = c1 = r2 = c2 = 0

        for row in range(5):
            for col in range(5):
                if m[row][col] == a:
                    r1 = row
                    c1 = col

                if m[row][col] == b:
                    r2 = row
                    c2 = col

        if r1 == r2:
            cipher += m[r1][(c1 + 1) % 5]
            cipher += m[r2][(c2 + 1) % 5]

        elif c1 == c2:
            cipher += m[(r1 + 1) % 5][c1]
            cipher += m[(r2 + 1) % 5][c2]

        else:
            cipher += m[r1][c2]
            cipher += m[r2][c1]

    return cipher


key = "college"
plaintext = "this is fergusson"

m = matrix(plaintext, key)

for row in m:
    print(row)

print("Ciphertext:", ciphertxt(plaintext, key))