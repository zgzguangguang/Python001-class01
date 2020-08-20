"""
容器序列：list、tuple、collections.deque

扁平序列：str、bytes、bytearray、memoryview、array.array

容器序列和扁平序列的区别？

容器序列可以存放不同类型的数据。即可以存放任意类型对象的引用。

扁平序列只能容纳一种类型。也就是说其存放的是值而不是引用。换句话说扁平序列其实是一段连续的内存空间，由此可见扁平序列其实更加紧凑。但是它里面只能存放诸如字符、字节和数值这种基础类型。

可变序列：列表，字典
不可变序列：元组，字符串

"""

def my_map(func,iterables):
    if hasattr(iterables,'__iter__'):
        for i in iterables:
            yield func(i)
    else:
        raise TypeError('{} object is not iterable'.format(iterables.__class__.__name__))


import time
from functools import wraps

def timer(func,*args,**kwargs):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        print ("运行时间: {}".format(end_time-start_time))
    return wrapper

