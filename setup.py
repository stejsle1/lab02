from setuptools import setup, find_packages


with open('README.rst') as f:
    long_description = ''.join(f.readlines())


setup(
   name='labelord_stejsle1',
   version='0.5',
   keywords='github repositories labels documentation test issue',
   description='Python command-line application for label handle on GitHub',
   long_description=long_description,
   author='Lenka Stejskalova',
   author_email='stejsle1@fit.cvut.cz',
   license='Public Domain',
   url='https://github.com/stejsle1/labelord',
   install_requires=[
        'Flask', 
        'click>=6', 
        'requests',
        'sphinx', 
   ],
   classifiers=[
        'Framework :: Flask',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Console',
        'Environment :: Web Environment',
        ],
   zip_safe=False,
   packages=find_packages(),
   package_data={'labelord': ['templates/*.html']},
   entry_points={
        'console_scripts': [
            'labelord = labelord:main',
        ],
   },    
)
