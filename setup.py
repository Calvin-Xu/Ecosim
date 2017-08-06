try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Natural environment simulation',
    'author': 'Calvin Xu',
    'url': 'https://github.com/Calvin-Xu/Ecosim',
    'download_url': 'https://github.com/Calvin-Xu/Ecosim',
    'author_email': 'calvinxu806@vip.163.com',
    'version': '1.0.0',
    'install_requires': ['pytest'],
    'packages': ['ecosim'],
    'scripts': [],
    'name': 'Ecosim'
}

setup(**config)
