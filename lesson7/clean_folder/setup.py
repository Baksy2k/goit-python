from setuptools import setup, find_packages

setup(
    name='clean-folder',
    version='1.0.0',
    description='clean-folder sorts all files to different folders judging by extention',
    url='http://',
    author='Baksy',
    author_email='baksy933@gmail.com',
    license='MIT',
    packages=find_packages(where="src"),
    #install_requires=['markdown'],
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean_folder:main']}
)