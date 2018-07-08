def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)
func(3, 7)
func(25, c=24) # 指定参数名来赋值
func(c=50, a=100) # 指定参数名来赋值