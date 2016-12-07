from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(name='checker',
      version='0.0.1',
      description=u"Raspberry Pi Build Checker",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author=u"Thiago Paes",
      author_email='mrprompt@gmail.com',
      url='https://github.com/mrprompt/raspberry-build-checker',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'click', 'travispy'
      ],
      extras_require={
          'test': ['pytest'],
      },
      entry_points="""
      [console_scripts]
      checker=checker.cli:cli
      """
      )
