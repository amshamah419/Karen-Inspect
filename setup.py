from setuptools import setup, find_packages

setup(
    name='karen-inspect',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'karen-inspect = karen.inspection:main',
        ],
    },
    description='A Python linter that flags "naughty" words and non-inclusive language to ensure code is HR compliant',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Amichai Shamah',
    author_email='amshamah@gmail.com',
    url='https://github.com/amshamah419/Karen-Inspect',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
