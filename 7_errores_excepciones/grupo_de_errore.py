#version 11
#errores = ExceptionGroup(OSError("error os"),ExceptionGroup(TypeError("error type")))
#raise errores

error = TypeError("type error")
#error.add_note('error add note')
#raise error

"""
def f():
    raise ExceptionGroup("group1",
                         [OSError(1),
                          SystemError(2),
                          ExceptionGroup("group2",
                                         [OSError(3), RecursionError(4)])])

try:
    f()
except* OSError as e:
    print("There were OSErrors")
except* SystemError as e:
    print("There were SystemErrors")
"""