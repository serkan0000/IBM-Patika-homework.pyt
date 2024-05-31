import math

def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def main():
    points = []
    n = int(input("Kaç nokta gireceksiniz? "))

    for i in range(n):
        x = float(input(f"Nokta {i+1} için x koordinatını girin: "))
        y = float(input(f"Nokta {i+1} için y koordinatını girin: "))
        points.append((x, y))

    distances = []

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = euclideanDistance(points[i], points[j])
            distances.append((i, j, distance))

    print("Mesafeler:")
    for (i, j, distance) in distances:
        print(f"Noktalar arasındaki mesafe {i+1} ve {j+1}:", distance)

if __name__ == "__main__":
    main()