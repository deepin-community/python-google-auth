# Copyright 2014 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import io

from setuptools import find_packages
from setuptools import setup


DEPENDENCIES = (
    'pyasn1-modules>=0.2.1',
    'rsa>=3.1.4',
    'six>=1.9.0',
    'cachetools>=2.0.0',
)


with io.open('README.rst', 'r') as fh:
    long_description = fh.read()

setup(
    name='google-auth',
    version='1.5.1',
    author='Google Cloud Platform',
    author_email='jonwayne+google-auth@google.com',
    description='Google Authentication Library',
    long_description=long_description,
    url='https://github.com/GoogleCloudPlatform/google-auth-library-python',
    packages=find_packages(exclude=('tests*', 'system_tests*')),
    namespace_packages=('google',),
    install_requires=DEPENDENCIES,
    license='Apache 2.0',
    keywords='google auth oauth client',
    classifiers=(
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
    ),
)
