from setuptools import setup

setup(
  name='pysteam',
  version='1.1.0-b2',
  description='Python library to work with Steam',
  url='http://github.com/scottrice/pysteam',
  author='Scott Rice',
  author_email='',
  license='MIT',
  packages=['pysteam'],
  install_requires=[
  ],
  data_files=[
  ],
  dependency_links=[
  ],
  zip_safe=False,
  test_suite='nose.collector',
  tests_require=[
    'nose',
    'parameterized',
    'mock',
  ],
)
