from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

setup(name              = 'ABElectronics_ADCPi',
      version           = '1.0.0',
      author            = '',
      author_email      = '',
      description       = 'Python Library to use with ADC Pi Raspberry Pi expansion board.',
      license           = '',
      url               = 'https://github.com/abelectronicsuk/ABElectronics_Python_Libraries',
      packages          = find_packages())