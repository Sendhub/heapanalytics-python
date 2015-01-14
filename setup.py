from distutils.core import setup, find_packages

setup(
    name='heapanalytics-python',
    version='0.1',
    packages=find_packages(),
    license=open('LICENSE').read(),
    author='Michael Palumbo',
    author_email='michael.palumbo87@gmail.com',
    description='HeapAnalytics Python library for server-side integration.',
    long_description=open('README.md').read(),
    keywords='heap analytics python',
)
