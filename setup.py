from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='rc_dynamics',
      version='0.0.1',
      description='Examples for parsing rc_dynamics messages from Roboception rc_visard',
      long_description=readme(),
      url='http://github.com/roboception/rc_dynamics_python',
      author='Felix Ruess',
      author_email='felix.ruess@roboception.de',
      license='BSD',
      packages=find_packages(),
      install_requires=['protobuf>=2.6.1'],
      include_package_data=True,
      entry_points={
        'console_scripts': ["rc_dynamics_listener = rc_dynamics.listener:main"]
      },
      zip_safe=False)
