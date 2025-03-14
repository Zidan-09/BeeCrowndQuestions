def locate(x, y, divx, divy):
    if x == divx or y == divy:
        return 'divisa'
    elif x < divx and y < divy:
        return 'SO'
    elif x > divx and y < divy:
        return 'SE'
    elif x > divx and y > divy:
        return 'NE'
    elif x < divx and y > divy:
        return 'NO'
    
while True:
    repetion = int(input())

    if repetion == 0:
        break
    
    divisor_point_x, divisor_point_y = map(int, input().split())
    for _ in range(repetion):
        x, y = map(int, input().split())

        print(locate(x, y, divisor_point_x, divisor_point_y))