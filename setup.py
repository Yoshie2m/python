from setuptools import setup

setup(
    name='pyhoge',
    version='0.1.0',
    package_dir={'': 'src'},
    packages=['user'],
    url='',
    license='',
    author='kyoshi',
    author_email='',
    description='test',
    entry_points={
        "console_scripts": [
            "thoge=user.user:abc"
        ]
    },
    python_requires='>=3.7',
)
