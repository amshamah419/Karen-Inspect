from setuptools import setup, find_packages

setup(
    name='python-hr-linter',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'karen-inspect = karen.inspection:main',
        ],
    },
    install_requires=[
        'click'
    ],
    description='A Python linter that is HR compliant and flags "naughty" words and non-inclusive language',
    author='Amichai Shamah',
    author_email='amshamah@gmail.com',
)
