from setuptools import find_packages, setup

package_name = 'gestion_maquette'

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
    maintainer='sharaf',
    maintainer_email='sharaf@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'vitesse_vent_publisher = gestion_maquette.vitesse_vent_publisher:main',
            'temperature_publisher = gestion_maquette.temperature_publisher:main',
            'humidite_publisher = gestion_maquette.humidite_publisher:main',
            'controle_led_subscriber = gestion_maquette.controle_led_subscriber:main',
            'controle_ventilateur_subscriber = gestion_maquette.controle_ventilateur_subscriber:main',
            'controle_deshumidificateur_subscriber = gestion_maquette.controle_deshumidificateur_subscriber:main',
        ],
    },
)

