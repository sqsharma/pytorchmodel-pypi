from setuptools import setup, find_packages


setup(
    name='pytorchmodel-pypi',
    version='2.0',
    license='Apache',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/sqsharma/pytorchmodel-pypi',
    keywords='pytorch model',
    install_requires=[
          'scikit-learn', 
      ],

)
