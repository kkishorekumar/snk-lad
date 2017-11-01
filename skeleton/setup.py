try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

config = {
    'description': 'Snakes and Ladders Game',
    'author': 'draKula',
    'url': 'NA',
    'download_url': 'NA',
    'author_email': 'draKula@HELL.COM',
    'version': '666',
    'install_requires': ['nose'],
    'packages': ['Snk_Lad'],
    'scripts': [],
    'name': 'Snake Game'
}

setup(**config)
