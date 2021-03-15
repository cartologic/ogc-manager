from distutils.core import setup

from setuptools import find_packages

long_description = open('README.md').read()
setup(
    name='osgeo-manager',
    packages=find_packages(),
    version='0.3.0',
    description='Cartoview is a GIS web mapping application framework to \
    easily share and deploy apps based on Geonode',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Cartologic',
    author_email='info@cartologic.com',
    url='https://github.com/cartologic/osgeo-manager',
    include_package_data=True,
    keywords=[
        'cartologic', 'cartoview', 'gis', 'geonode', "django", "web mapping", "applications",
        "apps", "application management"
    ],
    classifiers=[
        "Development Status :: 4 - Beta", "Framework :: Django :: 1.8",
        "Topic :: Scientific/Engineering :: GIS"
    ],
    license="BSD",
)
