from setuptools import find_packages, setup

from typing import List


HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this funtion will read line by line each library and help to create a string like : pin intall pandas.
    which will install all algorithm one by one in our environment.
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        '''
        while reading file line by line \n will be appear. we have to replace that
        '''
        requirements=[req.replace("\n","") for req in requirements]
        '''
        Now as we have added -e. to directly trigger setup.py . but we should remove from strings in requirements
        it also create new folder with project and packages information automatically.
        '''
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements
        


setup(
    name="ml_cluster",
    version="0.0.1",
    author="Pawan Singh",
    author_email="pawancse11@gmail.com",
    packages=find_packages(),
    install_require =get_requirements('requirements.txt')
)

