import sys

from setuptools import setup, find_packages


with open('requirements.txt') as f:
    requirements = f.read().splitlines()

if sys.version_info < (3, 6):
    requirements.append('argparse')

with open('README.md') as f:
    long_description = f.read()

setup(name='backend',
      version='0.1b0',
      description='Backend API',
      author='Walter Baidal',
      author_email='walterbaidal96@gmail.com',
      install_requires=requirements,
      # packages=find_packages('.', exclude=["test", "tests"]),
      packages=find_packages('.'),
      # package_data={'': ['config.ini']},  Agregar archivos no python
      include_package_data=True,
      license='Apache License 2.0',
      classifiers=[
          "Development Status :: 1 - Beta",
          "Environment :: Real-Time Mask Detection",
          "License :: OSI Approved :: Apache Software License",
          "Natural Language :: English",
          "Operating System :: POSIX :: Linux",
          "Programming Language :: Python :: 3.9",
          "Topic :: Backend API"
      ],
      python_requires='>=3.6',

      entry_points='''
                '''
      )
