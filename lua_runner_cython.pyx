cdef extern from "lua_runner.h":
    cdef int myfunc()

def callCfunc():
    print(myfunc())


