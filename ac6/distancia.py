x1, y1 = [float(x) for x in input().split(" ")]
x2, y2 = [float(x) for x in input().split(" ")]

distancia = ((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1)) ** 0.5

print(f"{distancia:.4f}")