from distutils.core import setup, Extension

module = Extension ( 'bitlib', libraries = ['BitLib'], sources = ['bitlibmodule.c'] )

setup ( name = "bitlib", version = "2.0", 
        maintainer = "codenio", maintainer_email = "aananthraj1995@gmail.com",
        description = "BitScope Library Python3 Extension module", ext_modules = [module] )
