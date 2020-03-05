import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
   name="prhplot-pavanhebbar",
   version="0.0.1",
   author="Pavan R. Hebbar",
   author_email="hebbar@ualberta.ca",
   description="Customized plotting package",
   long_description=long_description,
   long_description_content_type="text/markdown",
   url="https://github.com/pavanhebbar/prhplot",
   packages=setuptools.find_packages(),
   classifiers=[
       "Programming Language :: Python :: 3",
       "License :: OSI Approved :: MIT License",
       "Operating System :: OS Independent",
   ],
   python_requires='>=3.6',
)
