from setuptools import setup, find_packages

setup(
    name='chatroom-python',
    version='0.1',
    description='A simple chatroom implementation in Python.',
    author='Ayush Jain',
    author_email='ayushj0909@outlook.com',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'start-server=server.server:start_server',
            'start-client=client.client:start_client',
        ],
    },
)
