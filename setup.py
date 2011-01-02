import distribute_setup
distribute_setup.use_setuptools()
from setuptools import setup, find_packages

setup(
    name = "Quick .Torrent Downloader",
    version = "0.1",
    packages = find_packages('.'),
    package_dir = {'':'.'},
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
        },
    author = "Michael Nussbaum",
    author_email = "michaelnussbaum08@gmail.com",
    description = "Command line tool to find and download .torrent files",
    long_description = "A command line tool that begins the torrenting" + \
      " process by searching for a given term and result name, " + \
      "downloading the .torrent file and opening it in your default " + \
      "BitTorrent client.",
    license = "LICENSE.txt",
    keywords = ["torrent", ".torrent downloader", '.torrent finder',
      ".torrent"],
    platform = "Any",
    url = "https://github.com/michaelnussbaum08/Quick-.Torrent-Downloader",
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python"
    ]
)
