from setuptools import find_packages, setup

setup(
    name="app",
    version="1.0.0",
    url="https://github.com/fdsmora/wl-rest-api",
    maintainer="Fausto Salazar",
    maintainer_email="fausto.ds.mora@gmail.com",
    description="Wizeline REST API for programming course",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["flask"],
    extras_require={"test": ["pytest"]},
)
