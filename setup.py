from setuptools import find_packages, setup
from typing import List

# Constants
HYPTHEN_E_DOT = "-e ."

def get_requirements(file_path: str = "requirements.txt") -> List[str]:
    '''
    Returns the list of requirements (required packages)
    '''
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        lines.remove(HYPTHEN_E_DOT)
    return lines

setup(
    name = "end_to_end_ml",
    version = "0.0.1",
    author = "Tashreque",
    author_email="tashrik.haque@gmail.com",
    packages = find_packages(),
    requires = get_requirements()
)