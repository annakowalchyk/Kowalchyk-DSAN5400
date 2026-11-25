import setuptools 
with open('README.md', 'r') as f: 
    long_description = f.read() 

setuptools.setup( 
    name='matcher', 
    version='0.0.1', 
    author='Anna Kowalchyk', 
    author_email='ark170@georgetown.edu', 
    description='DSAN5400 Assignment 4', 
    long_description=long_description, 
    long_description_content_type='text/markdown', 
    packages=setuptools.find_packages(), 
    python_requires='>=3.6', 
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'matplotlib',
        'Levenshtein',
        'jarowinkler'
    ],
    extras_requires={"dev": ["pytest", "flake8", "autopep8"]}, 
) 