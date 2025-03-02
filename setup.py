from setuptools import setup

setup(
    name="madiff_testing",
    description="Multi-agent Diffusion Model.",
    packages=["diffuser"],
    package_dir={
        "diffuser": "./diffuser",
    },
)
