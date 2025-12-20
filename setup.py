from setuptools import find_packages, setup
from typing import List

def get_requirements(filepath: str)->List[str]:
    '''
    this function returns a list of packages required
    :filepath is the path where the packages are listed
    '''
    requirements:List[str] = []
    with open(filepath) as f:
        #ignore the last line -e .
        requirements = [req.replace("\n", "") for req in f.readlines()[:-1]]
    
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='krish',
    author_email='krishnaik06@gmail.com',
    packages=find_packages(),
    requires=get_requirements('requirements.txt')
)