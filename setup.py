from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requiremts=file_obj.readlines()
        [req.replace('\n','') for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')
    
    return requirements

setup(
    name='mlproj_template',
    version='0.0.1',
    author='Vipulesh',
    author_email='tiwarivipulesh@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)