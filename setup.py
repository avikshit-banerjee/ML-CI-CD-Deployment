from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements

    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements= [req.replace("/n", "") for req in requirements] #for getting rid of the /n which will be read as well 

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(

name= 'MLproject',
version= '0.0.1',
author= 'Avikshit',
author_email= 'avikshitbanerjee@gmail.com',
packages=find_packages(),
requires = get_requirements('requirements.txt')

)

