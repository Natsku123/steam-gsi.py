from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='steam_gsi',
   version='0.1',
   description='Steam GSI Framework for Python',
   license="",
   long_description=long_description,
   author='Max Mecklin',
   author_email='max@meckl.in',
   url="https://github.com/Natsku123/steam-gsi.py",
   packages=['steam_gsi'],
   install_requires=['aiohttp'],
   scripts=[]
)
