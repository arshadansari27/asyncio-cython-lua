from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize

'''
setup(
      name = 'LuaCall',
      ext_modules=[
              Extension(
                  'lua_runner_cython', 
                  ['lua_runner_cython.pyx'],
                  sources=["lua_runner.c"],
                  language="c"
              )
              ],
      cmdclass = {'build_ext': build_ext}
)
'''
#python setup.py build_ext --inplace
#python3 setup.py build_ext --inplace
setup(name="LuaCall", ext_modules = cythonize(
               "lua_runner_cython.pyx",                 # our Cython source
               sources=["lua_runner.h"],  # additional source file(s)
               language="c",             # generate C++ code
))
