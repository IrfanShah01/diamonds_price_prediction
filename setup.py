from setuptools import find_packages
from setuptools import setup
from typing import List

Hypen_e_dot = '-e .'

def get_requirments(file_path:str):
    requirments = []
    with open(file_path) as file_object:
        requirments = file_object.readlines()
        requirments = [req.replace("\n","") for req in requirments]
        
        if Hypen_e_dot in requirments:
            requirments.remove(Hypen_e_dot)
            
        return requirments
    


setup(
    
    name = 'Regressor_Project',
    version = '0.0.1',
    author = 'Fannay',
    author_email = 'fannay@gmail.com',
    install_requires = get_requirments('requirments.txt'),
    packages = find_packages()
    
)