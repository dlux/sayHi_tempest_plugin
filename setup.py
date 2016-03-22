# Setuptools is used to facilitate packaging
# Python projects.

from setuptools import setup, find_packages

setup(
    # Package details
    name = 'dluxsay',
    version = '0.1.0',
    packages = find_packages(),

    #metadata for upload to PyPI
    description = 'Packaging a python say_hi demo project',
    author = 'Luz Cazares',
    author_email = 'tmp@dlux.com',
    url = 'https://github.com/dlux/sayhi_package_demo',
    test_suite='demo.tests',
    keywords = ['dlux', 'say_hi', 'hello_world', 'mypackage'],

    # Additional metadata
    classifier = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Quality Engineers',
        'Intended Audience :: Information Technology',
        'License :: Free For Educational Use',
        'Operating System :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        ],
    entry_points = {
         'console_scripts':[
             'dluxsay = demo.src.say_hi:main',
             ],
         # Tempest plugin
         'tempest.test_plugins':[
             'dluxsay-TP = demo_tempest_plugin.plugin:sayHiPlugin',
             ],
         }
)

