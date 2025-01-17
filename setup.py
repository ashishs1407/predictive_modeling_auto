from setuptools import setup,find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name = "pyc_regressor",
    version= '0.0.2',
    description="This is a pycaret regressor package.",
    long_description=long_description
    LONG_DESCRIPTION = '''
                        [github repo - ](https://github.com/ashishs1407/predictive_modeling_auto)
                        ''',
    author="Ashish Shimpi",
    author_email="a.shimpi93@gmail.com",
    packages = find_packages(),
    url='https://github.com/ashishs1407/predictive_modeling_auto'
    py_modules=[],
    keywords=['python', 'tutorial', 'Auto-regressor', 'ashish shimpi'],
    project_urls={
    'Source': 'https://github.com/ashishs1407/predictive_modeling_auto',
    'Tracker': 'https://github.com/ashishs1407/predictive_modeling_auto/issues',
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
                    
    ],
    python_requires='>=3.6',

)