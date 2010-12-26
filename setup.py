import distribute_setup
distribute_setup.use_setuptools()
from setuptools import setup, find_packages

setup(
    name = "Quick .Torrent Downloader",
    version = "0.1",
    packages = find_packages('src'),
    package_dir = {'':'src'},
    include_package_data = True,
    install_requires = ['BeautifulSoup>=3.2'],
    entry_points={
        'console_scripts': [
            'qtd = src.qtd:main',
        ]
    },
    test_suite = "tests",
    package_data = {
        '': ['*.txt'],
        }

    author = "Michael Nussbaum",
    author_email = "michaelnussbaum08@gmail.com",
    description = "Command line tool to find and download .torrent files",
    license = "BSD",
    keywords = "torrent downloader finder .torrent",
)
