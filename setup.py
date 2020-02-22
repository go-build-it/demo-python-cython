from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='hello',
    python_requires=">=3.6",
    ext_modules=cythonize("hello.pyx"),
)
