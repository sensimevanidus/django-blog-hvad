import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-blog-hvad',
    version='0.1',
    packages=['blog_hvad',],
    include_package_data=True,
    license='Apache License, Version 2.0',
    description='Simple yet useful Django application used to create a beautiful blog for free.',
    long_description=README,
    url='https://github.com/sensimevanidus/django-blog-hvad',
    author='Onur Yaman',
    author_email='onuryaman+django_blog_hvad@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache License, Version 2.0',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)