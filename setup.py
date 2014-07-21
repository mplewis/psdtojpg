from setuptools import setup

with open('README.rst') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    install_requires = f.read().split('\n')

setup(
    name='psdtojpg',
    version='0.1.0',
    description='Convert one or more PSD files to JPG format. Thumbnail and '
                "optimize them, or don't.",
    long_description=long_description,
    url='https://github.com/mplewis/psdtojpg',
    license='MIT',
    author='Matthew Lewis',
    author_email='matt@mplewis.com',
    py_modules=['psdtojpg'],
    entry_points={
        'console_scripts': [
            'psdtojpg = psdtojpg:main'
        ]
    },
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion'
    ],
    install_requires=install_requires
)
