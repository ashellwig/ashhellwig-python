from setuptools import setup
from distutils.util import convert_path

from typing import Dict, Any

# Version Information
main_ns: Dict[Any, Any] = {}
version_path = convert_path('ashhellwig-python/version.py')
with open(version_path) as version_file:
    exec(version_file.read(), main_ns)

# Long Description via README.md
with open('README.md', 'r') as fh:
    long_description: str = fh.read()

setup(name='ashhellwig-python',
      version=main_ns['__version__'],
      description='''
        Flask + GraphQL API server implementation of Ash Hellwig's personal
        website.
        ''',
      long_description=long_description,
      url='https://github.com/ashellwig/ashhellwig-python',
      packages=['ashhellwig-python'],
      console_scripts=['ashhellwig-python=ashhellwig-python:main'],
      include_package_data=True,
      zip_safe=False,
      classifiers=[
          'Development Status :: 1 - Planning', 'Environment :: Console',
          'License :: OSI Approved :: GNU Affero General Public License v3',
          'Natural Language :: English',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3 :: Only', 'Typing :: Typed'
      ])
