#!/usr/bin/env python
# coding: utf-8
from ophyd import Device, EpicsSignal, EpicsSignalRO
from ophyd import Component as Cpt
#from ophyd.log import config_ophyd_logging

class EGun(Device):
    firmware_revision = Cpt(EpicsSignalRO, 'getFirmwareRevision')
    model_name = Cpt(EpicsSignalRO, 'getName')
    model_revision = Cpt(EpicsSignalRO, 'getModelRevision')
    model_config = Cpt(EpicsSignalRO, 'getModelConfig')
    serial_number = Cpt(EpicsSignalRO, 'getSerialNumber')
    status = Cpt(EpicsSignalRO, 'getStatus')
    source_output = Cpt(EpicsSignal, 'getSourceOutput', write_pv='setSourceOutput')
    source_input = Cpt(EpicsSignalRO, 'getSourceInput') 
    grid_output = Cpt(EpicsSignal, 'getGridOutput', write_pv='setGridOutput')
    grid_input = Cpt(EpicsSignalRO, 'getGridInput') 
    first_anode_output = Cpt(EpicsSignal, 'getFirstAnodeOutput', write_pv='setFirstAnodeOutput')
    first_anode_input = Cpt(EpicsSignalRO, 'getFirstAnodeInput')
    focus_output = Cpt(EpicsSignal, 'getFocusOutput', write_pv='setFocusOutput')
    focus_input = Cpt(EpicsSignalRO, 'getFocusInput')
    ecc_output = Cpt(EpicsSignal, 'getECCOutput', write_pv='setECCOutput')
    energy_input = Cpt(EpicsSignalRO, 'getEnergyInput')
    emission_current_input = Cpt(EpicsSignalRO, 'getEmissionCurrentInput')
    source_current_input = Cpt(EpicsSignalRO, 'getSourceCurrentInput')
    is_panel_enabled = Cpt(EpicsSignal, 'setPanelEnable')
    is_debug_enabled = Cpt(EpicsSignal, 'setDebugEnable')
    reset_device = Cpt(EpicsSignal, 'reset')
    save_device = Cpt(EpicsSignal, 'save')
    resume_device = Cpt(EpicsSignal, 'resume')
    shutdown_device = Cpt(EpicsSignal, 'shutdown')
        
        
    def stage(self):
        self.resume_device.get()
        self.is_debug_enabled.set(1)
        self.save_device.get()
        self.wait_for_connection()
        super().stage()
        
        
    def unstage(self):
        self.save_device.get()
        self.is_debug_enabled.set(0)
        self.save_device.get()
        self.wait_for_connection()
        super().unstage()
    
    
    def set_parameter_voltage(self, value, output_object, input_object, name, unit):
        if self.status.get()==1:
            self.stage()
            output_object.set(value)
            self.unstage()
            return print(name, " voltage(",unit,") is set to = ", output_object.get(), 
                         "\n The real ",name," energy(",unit,") is on =", input_object.get())
        else:
            return print("Device status is off.")
          
        
    def print_device_info(self):
        return print("EGun Specifications:\n",
                     "\n"+"Firmware Revision = ",self.firmware_revision.get(),
                     "\n"+"Model Name = ",self.model_name.get(),
                     "\n"+"Model Revision = ",self.model_revision.get(),
                     "\n"+"Model Config = ",self.model_config.get(),
                     "\n"+"Serial Number = ",self.serial_number.get(),
                     "\n"+"Channel 1 Output = ",self.channel_one_output.get(),
                     "\n"+"Channel 1 Input = ",self.channel_one_input.get())