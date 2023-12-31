x, y = 3427, 12262

spline = []

def collateLine(point):
    global x, y
    spline.append((x, y, x + point[0], y + point[1]))
    x += point[0]
    y += point[1]

def collateBezier(command):
    global x, y
    spline.append((x, y, x+command[0], y+command[1], x+command[2], y+command[3]))
    x += command[2]
    y += command[3]

# lines = [int(c) for c in "-27 -28 0 -426 0 -427 53 -5".split()]
# for i in range(len(lines) // 2):
#     point = lines[i*2:i*2+2]
#     collateLine(point)


# beziers = [[int(c) for c in li.split()] for li in """28 -4 115 -13 192 -22
# 518 -56 882 -161 1031 -297
# 144 -131 221 -375 245 -777
# 15 -262 7 -6792 -10 -6960
# -54 -559 -131 -910 -266 -1209
# -218 -484 -555 -755 -1023 -822
# -113 -16 -387 -7 -472 16
# -155 41 -318 139 -371 223
# -48 76 -43 92 63 191
# 295 275 412 415 507 606
# 110 220 147 396 138 659
# -13 409 -139 710 -411 982
# -205 205 -419 320 -714 387
# -85 19 -127 21 -332 21
# -254 0 -346 -12 -520 -70
# -490 -164 -874 -605 -989 -1135
# -46 -215 -53 -548 -16 -788
# 73 -467 269 -857 594 -1181
# 320 -319 761 -566 1266 -708
# 607 -172 1396 -215 2180 -121
# 570 69 1092 217 1546 440
# 366 180 655 383 919 649
# 477 478 729 1037 825 1830
# 22 185 44 471 51 675
# 3 99 7 196 9 215
# 2 19 5 1396 5 3060
# 1 1678 6 3074 11 3135
# 26 320 94 544 203 671
# 128 150 454 256 964 314
# 95 11 178 22 183 25
# 6 4 9 168 9 425""".split('\n')]
# for i in range(len(beziers)):
#     collateBezier(beziers[i])

# lines = [int(c) for c in "-1 419 -25 31 -26 30 -2882 0 -2882 0 -27 -28".split()]
# for i in range(len(lines) // 2):
#     point = lines[i*2:i*2+2]
#     collateLine(point)

# print(spline)

x, y = 0, 0
beziers = [[int(c) for c in d.split()] for d in """100 -400 200 0
400 100 0 200
-100 400 -200 0
-400 -100 0 -200""".split('\n')]

for i in range(len(beziers)):
    collateBezier(beziers[i])

print(spline)