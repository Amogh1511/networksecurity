"""
The setup.py file is essential for packaging and distributing python projects.
Used for set up tools, define configuration of the project, metadata, dependencies and more.
"""
import setuptools 
from setuptools import find_packages, setup
from typing import List

hypen="-e ."
def get_packages()->List:
    # This function will give list of packages
    packagesList:List[str]=[]
    try:
        with open("packages.txt", "r") as file:
          # Reading line in packages.txt and process each line
          lines=file.readlines()
          for line in lines:
              package=line.strip()
              # Ignoring hypen
              if package and package!= hypen:
                  packagesList.append(package)
    except FileNotFoundError:
        print("package.txt file not found")
    
    return packagesList

setup(
    name="networksecurityproject",
    version= "0.0.1",
    author="Amogh",
    author_email="amoghmath2000@gmail.com",
    packages=find_packages(),
    install_requires = get_packages()   
)
