from setuptools import setup

package_name = 'my_diffbot_ctrl'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools'],
    entry_points={
        'console_scripts': [],
    },
)