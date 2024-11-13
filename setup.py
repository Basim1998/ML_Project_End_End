from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    this function reads the requirements file and returns a list of requirements
    '''
    requirements = []
    with open(file_path) as fileobj:
        requirements = fileobj.readlines()
        requirements = [r.replace('\n', '') for r in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='ML_Project',
    version='0.1',
    author='Basim',
    author_email='basimaslamvk98@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)