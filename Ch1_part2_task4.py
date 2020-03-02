# t = int(input())
#     if hour == 60
#         return hour
#     elif minutes == 60
#         return minutes
#     elif seconds == 60
#         return 60
#     else:
#         return 60

# a = int(input())
# b = float(input())
# print(a, b)

# seconds1 = int(input())
# minutes1 = int(input())
# hours1 = int(input()) 
# seconds2 = int(input()) 
# minutes2 = int(input()) 
# hours2 = int(input())

# total1 = minutes1 * 60 + hours1 * 3600 + seconds1

# total2 = minutes2 * 60 + hours2 * 3600 + seconds2
# print(total2 - total1)

num_hours1 = int(input())
num_min1 = int(input())
num_sec1 = int(input())
num_hours2 = int(input())
num_min2 = int(input())
num_sec2 = int(input())
print(((num_hours2-num_hours1)*3600)+((num_min2-num_min1)*60)+(num_sec2-num_sec1))