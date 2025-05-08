from setuptools import setup,find_packages
from typing import List

def get_requirements(file_path:str)->List:
    '''
    This function will read the requirements.txt file and return a list of packages
    '''
    requirements = []
    hypen = '-e .'
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace('\n','') for req in requirements]
    if hypen in requirements:
        requirements.remove(hypen)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Abhilash Ky',
    author_email='ky.abhilashise@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)