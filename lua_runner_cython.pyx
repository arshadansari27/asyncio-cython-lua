cdef extern from "lua_runner.h":
    cdef int myfunc()

def callCfunc():
    return myfunc()


