from setuptools import setup, find_namespace_packages

with open("README.md") as file:
    read_me_description = file.read()

setup(name='clean-folder',
      version='1',
      description="This is a test package.",
      long_description=read_me_description,
      long_description_content_type="text/markdown",
      url='https://github.com/Serhii-Olkhovskyi/GoIT/tree/master/GoIT_Home_Work_2',
      author='Serhii Olkhovskyi',
      author_email='programing.sergii@gmail.com',
      license='MIT',
      packages=['clean-folder'],
      python_requires='>=3.5',
entry_points = {'console_scripts': ['clean-folder = clean-folder.clean:run',]}

)
