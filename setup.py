import subprocess
import os
from setuptools import setup, find_packages


def get_version():
    version = "0.0.1"  # Default version if no git tag is found
    try:
        # Try to get the current Git tag
        version = subprocess.check_output(["git", "describe", "--tags", "--abbrev=0"]).strip().decode('utf-8')
    except Exception:
        pass

    # Write the version to your_package/__version__.py so that it's available in the installed package
    with open(os.path.join("django_daisy", "__version__.py"), "w") as version_file:
        version_file.write(f'__version__ = "{version}"\n')

    return version


setup(
    name='django_daisy',
    version=get_version(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],  # Add dependencies here
    description='A modern django dashboard built with daisyui',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/hypy13/django-daisy',
    author='Hossein Yaghoubi',
    author_email='hossein.yaghoubi13@gmail.com',
    license='Apache 2.0',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
)
