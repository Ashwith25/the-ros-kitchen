from setuptools import find_packages, setup

package_name = 'part1'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ash',
    maintainer_email='pashwith25@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'chef = part1.chef:main',
            'waiter = part1.waiter:main',
            'manager = part1.manager:main',
        ],
    },
)
