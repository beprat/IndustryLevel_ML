from setuptools import find_packages,setup
from typing import List

# setup.py makes your project behave like a proper Python package — 
# installable,reusable, deployable, and cleanly structured.
# setup.py is used to package your project, so it can be installed and reused like any other Python library

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the lst of requirements.
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:  # Kyuki HYPEN_E_DOT install na ho(Beacuse this was only to trigger setup.py)
            requirements.remove(HYPEN_E_DOT)

    return requirements



setup(
    name='mlproject',
    version='0.0.1',
    author="Pratyush",
    author_email="beherapratyush2@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
