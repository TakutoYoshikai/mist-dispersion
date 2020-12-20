from setuptools import setup, find_packages

setup(
    name = 'mist_dispersion',
    version = '1.0.0',
    url = 'https://github.com/TakutoYoshikai/mist-dispersion.git',
    license = 'MIT LICENSE',
    author = 'Takuto Yoshikai',
    author_email = 'takuto.yoshikai@gmail.com',
    description = 'mist-dispersion is a disperser of any file data.',
    install_requires = ['setuptools', "lina@git+https://github.com/TakutoYoshikai/lina.git"],
    packages = find_packages(),
    entry_points={
        "console_scripts": [
            "mist-dispersion = mist_dispersion.mist_dispersion:main",
        ]
    }
)
