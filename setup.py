# -*- coding: utf-8 -*-

from distutils.core import setup

for line in open('neurotune/__init__.py'):
    if line.startswith("__version__"):
        version = line.split("=")[1].strip()[1:-1]
        
setup(
    name = "neurotune",
    version = version,
    packages = ['neurotune'],
    author = "Michael Vella, Padraig Gleeson",
    author_email = "mv333@cam.ac.uk, p.gleeson@gmail.com",
    description = "A Python library for optimising neuronal models",
    license = "BSD",
    url='https://github.com/NeuralEnsemble/neurotune',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering']
)



