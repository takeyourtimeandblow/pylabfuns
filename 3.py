def is_triangle(a, b, c):
    return all([a + b > c, b + c > a, a + c > b])


try:
    triangle = list(map(int, input().split(' ')))[:3]
    print(is_triangle(triangle[0], triangle[1], triangle[2]))
except IndexError:
    print("not enough values")
