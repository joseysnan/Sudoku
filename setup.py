from setuptools import setup, find_packages

setup(
    name="my_sudoku_game",               # Your package name (must be unique on PyPI)
    version="0.1.0",                     # Version number (follow semantic versioning)
    description="A basic 4x4 Sudoku game implemented in Python",
    long_description=open("README.md").read(),  # Long description (from README)
    long_description_content_type="text/markdown",  # Format of the long description
    author= "Josepha Nangmo",                  
    author_email="jnangmo0@gmail.com",  
    url="https://github.com/username/my_sudoku_game",  # Project's GitHub URL
    license="MIT",                       
    packages=find_packages(),            # Automatically find packages in the project
    install_requires=[],                 # List of dependencies (e.g., ["numpy", "requests"])
    python_requires=">=3.7",            
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "sudoku_game=my_package.main:main",  # Command to run your program
        ],
    },
)
