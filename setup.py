from setuptools import setup

__version__ = 0.2
__doc__ = """Simplify login to Pocket"""

setup(
 name = "pocket_login",
 version = __version__,
 description = __doc__,
 py_modules = ["pocket_login"],
 install_requires = [
  'pocket',
 ],
 classifiers = [
  'Development Status :: 4 - Beta',
  'Intended Audience :: Developers',
  'Programming Language :: Python',
  'License :: OSI Approved :: MIT License',
  'Topic :: Software Development :: Libraries',
 ],
)
