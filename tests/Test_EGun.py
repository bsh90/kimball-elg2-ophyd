import sys
sys.path.append('/.../src')

import unittest
from EGun import EGun


class TestSmarPod(unittest.TestCase):

    def test_set_source_energy(self):
        prefixSISSYANAEX = 'SISSYANAEX:EGUN00:'
        e_gun = EGun(prefixSISSYANAEX, name='eGunTest')
        e_gun.wait_for_connection()

        e_gun.print_device_info()
        #config_ophyd_logging(level='DEBUG')
        selectedSourceEnergy = 2
        e_gun.set_parameter_voltage(value=selectedSourceEnergy, output_object=e_gun.source_output, 
                                    input_object=e_gun.source_input, name="Source", unit="mV")
