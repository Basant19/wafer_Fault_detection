from setuptools import find_packages,setup
from typing import List 


HYPEN_E_DOT = '-e .'

def get_requirements (file_path:str) ->List[str]:
    '''
    Reads the requirements.txt file.
    Stores all dependencies (packages) listed in the file into a list.
    Removes any newline characters ("\n") from each requirement.
    Returns the cleaned list of package names.

    '''
    requirements=[]
    with open (file_path) as file_obj:
                        
            requirements=file_obj.readlines()
            '''
            in requirements.txt file is stored in this format so we have to remove 
            ["pandas/n","numpy/n"]
            '''
            requirements=[req.replace("/n","") for req in requirements]
            if HYPEN_E_DOT in requirements:
                  requirements.remove (HYPEN_E_DOT )
            

          
    return requirements    

setup (
    name="Wafer_fault_detection",
    version="1.0.0",
    author="Basant Tirkey",
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt'),
    
)