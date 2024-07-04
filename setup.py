from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()
    
setup(
    name='deploy_helper',
    version='0.1',
    packages=['deploy_helper'],
    install_requires=requirements,
    entry_points = {
        'console_scripts': ['dh=deploy_helper.main:main'],
    },
)