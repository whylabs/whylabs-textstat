from setuptools import setup
from io import open

setup(
    name='whylabs-textstat',
    packages=['textstat'],
    version='0.7.4',
    description='Calculate statistical features from text',
    author='Shivam Bansal, Chaitanya Aggarwal',
    author_email='shivam5992@gmail.com',
    url='https://github.com/whylabs/whylabs-textstat',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    package_data={'': ['easy_word_list']},
    include_package_data=True,
    install_requires=['setuptools', 'syllapy'],
    license='MIT',
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3 :: Only",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Text Processing",
    ],
)
