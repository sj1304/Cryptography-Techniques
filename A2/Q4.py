def rail_fence_encrypt(text, rails):
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    for ch in text:
        fence[rail].append(ch)
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction *= -1
    return ''.join(''.join(row) for row in fence)

print(rail_fence_encrypt("tomorrow is tuesday".replace(" ",""),4))
