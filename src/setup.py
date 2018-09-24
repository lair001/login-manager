import setuptools

setuptools.setup(
    name="login_manager",
    author="Samuel Lair",
    author_email="lair001@gmail.com",
    version="0.0.1",
    license="MIT",
    url="https://github.com/lair001/data-structures-and-algorithms-in-python-solutions",
    description="A tool for managing SSH credentials.",
	entry_points={
        'console_scripts': ['lgn = login_manager.LoginManager:main']
	},
    packages=setuptools.find_packages()
)
