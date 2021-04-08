def open_or_senior(data):
    result = []
    for list in data:
        if list[0] >=55 and list[1] > 7:
            result.append("Senior")
        else:
            result.append("Open")
        
    return result

print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))
print(open_or_senior([(16, 23),(73,1),(56, 20),(1, -1)])
