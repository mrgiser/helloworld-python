while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
        # 任何相应循环中的 else块都将不会被执行
    print('Length of the string is', len(s))
else:
    print("else print")
print('Done')