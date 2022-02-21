str = input()

left = str.split("(^0^)")[0].count("@")
right = str.split("(^0^)")[1].count("@")
print(left, right)