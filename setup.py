import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name = 'amphi',
    packages = ["amphi"],
    version = '1.0.9',
    license='MIT',
    description = 'MoviePy OOP wrapper',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = 'Rodney Maniego Jr.',
    author_email = 'rod.maniego23@gmail.com',
    url = 'https://github.com/rmaniego/amphi',
    download_url = 'https://github.com/rmaniego/amphi/archive/v1.0.tar.gz',
    keywords = ['MoviePy', 'Video', 'Editor'],
    install_requires=['moviepy', 'vidstab', 'sometime'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers', 
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    python_requires='>=3.6'
)