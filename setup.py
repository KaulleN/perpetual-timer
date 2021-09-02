import setuptools

with open('README.md') as f:
    readme = f.read().strip()

setuptools.setup(
    name='perpetual-timer',
    version='1.0.1',
    description='A thread that runs endlessly until stopped with a specified interval between iterations',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/KaulleN/perpetual-timer',
    author='Gleb Nikolaev',
    maintainer='Gleb Nikolaev',
    package_dir='',
    packages=['perpetual_timer'],
    python_requires='>=3.6',
    install_requires=[],
)
