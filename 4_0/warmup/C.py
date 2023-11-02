import math

xa, ya, xb, yb = map(int, input().split())

ra = (xa ** 2 + ya ** 2) ** 0.5
rb = (xb ** 2 + yb ** 2) ** 0.5

if xa == xb and ya == yb:
    dist = 0
elif (xa == 0 and ya == 0) or (xb == 0 and yb == 0):
    dist = max(ra, rb)
elif xa == 0 and xb == 0:
    dist = abs(ya - yb)
elif ya == 0 and yb == 0:
    dist = abs(xa - xb)
elif xa == 0:
    dist1 = ra + rb
    phi = math.pi / 2 - math.atan2(yb, xb)
    dist2 = phi * min(ra, rb) + abs(ra - rb)
    dist = min(dist1, dist2)
elif xb == 0:
    dist1 = ra + rb
    phi = math.pi / 2 - math.atan2(ya, xa)
    dist2 = phi * min(ra, rb) + abs(ra - rb)
    dist = min(dist1, dist2)
else:
    dist1 = ra + rb
    phi1 = math.atan2(ya, xa)
    phi2 = math.atan2(yb, xb)

    phi = phi2 - phi1
    while phi > math.pi:
        phi -= 2 * math.pi
    while phi < -math.pi:
        phi += 2 * math.pi

    dist2 = abs(phi) * min(ra, rb) + abs(ra - rb)
    dist = min(dist1, dist2)

print('{:.12f}'.format(dist))
