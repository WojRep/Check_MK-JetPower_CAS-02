#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-
#
from .agent_based_api.v1 import *
import pprint


def discover_jetpower(section):
    pprint(section)
    yield Service(item="zzz")

def check_jetpower(item, section):
    pprint(item)
    pprint(section)
    yield Result(state=State.OK, summary="", notice="", details="")
    return



register.snmp_section(
    name="jetpower",
#    detect = matches(".1.3.6.1.2.1.1.2.0", ".*(54321|38747).*"),
     detect = contains(".1.3.6.1.2.1.1.2.0", "54321"),
    fetch = SNMPTree(
        base = '.1.3.6.1.4.1.38747.1',
        oids = [
            "2.0",  # Model name
            "3.0",  # Firmware version
            "4.0",  # Site name
            "5.0",  # System status: 1-normal, 2-minor alarm, 3-major alarm
            "6.0",  # System voltage
            "7.0",  # Systen current
            "8.0",  # AC voltage
            "9.0",  # Battery number
            "11.0", # Battery current: <0 - discharge, >0 - charge battery
            "12.0", # Battery capacity in %
            "13.0", # Status of battery work: 1 float charge, 2 - equalize charge
            "14.0", # Rectifiers numbers
            "15.0", # Rectifiers communication agent status: 1 - normal, 2 - interupt
            "16.0", # Rectifiers Output Voltage
            "17.0", # Rectifiers Output Current
            "18.0", # Rectifiers Output Current limit
            "19.0", # Rectifiers Input Voltage
            "20.0", # Rectifiers Status: 0 - shutdown, 1 - power on
            "21.0", # Rectifiers PugIn OK: 0 - normal, 1 - alarm
            "22.0", # HVSD - Over Voltage: 0 - normal, 1 - alarm
            "23.0", # Rectifiers Output status: 0 - normal, 1 -alarm
            "24.0", # Rectifiers Input Over Voltage: 0 - normal, 1 - alarm
            "25.0", # Rectifiers Input Under Voltage: 0 - normal, 1 - alarm
            "26.0", # FAN status: 0 - normal, 1 - alarm
            "27.0", # Ambient Over temperature: 0 - normal, 1 - alarm
            "28.0", # Ambient Under temperature: 0 - normal, 1 - alarm
            "29.0", # Rectifiers PFC temperature: 0 - normal, 1 - alarm too hight
            "30.0", # Rectifiers DHDH temperature: 0 - normal, 1 - alarm too hight
            "31.0", # Status of communications between rectifiers: 0 - normal, 1 - unsuccessful
            "32.0", # DCDC eeprom status: 0 - normal, 1 - fault
            "33.0", # the output power is whtaher derated by the ac voltage or not: 0 - normal, 1 - alarm
            "34.0", # the output power is whther derated by the temperature or not: 0 - normal, 1 - alarm
            "35.0", # the status of the rectifier current shared with other rectifier whether ok or not: 0 - normal, 1 - alarm
            "36.0", # PFC eeprom status: 0 - normal, 1 - fault
            "37.0", # the status of the communication between the recitifiers and the monitor: 0 - normal, 1 - alarm
            "38.0", # whether the AC voltage is normal or not: 0 - normal, 1 - out of the range
            "39.0", # whether the output of the rectifier is normal or not: 0 - normal, 1 - alarm
            "40.0", # whether the current of the battery is higher than the standard current which set up: 0 - normal, 1 - alarm
            "41.0", # whether the temperature of the battery is normal or not: 0 - normal, 1 - alarm
            "42.0", # the fuse of the battery loop: 0 - well, 1 - broken
            "43.0", # the number of the load in the system
            "44.0", # the fuse of the load loop: 0 - well, 1 - broken
            "45.0", # BLVD --the battery low voltage disconnected: 0 - connected, 1 - disconnected
            "46.0", # The digital input status of the DI port,0x01 indicates DI0 and 0x02 indicates DI1, and so on
            "47.0", # The sum of active alarms
            # "56.0", # the float voltage of the battery,get in V.
            # "57.0", # the EQ voltage of the battery,get in V
            # "58.0", # the maxinum of the battery current which make alarm , get in (A)
            # "59.0", # LLVD the voltage which the power system unload  get in V
            # "60.0", # BLVD--the protected voltage which the power system unload the battery   get in V
            # "61.0", # the limit current of the battery in EQ charge mode
            # "62.0", # the period of the next EQ charge time
            # "63.0", # the battery temperature which make alarm. get in Celsius degree
            # "64.0", # the capacity of the battery in the power system. get in Ah
            # "65.0", # the in all time of the battery in EQ charge mode. get in minute.
            # "66.0", # the total time of the stable current in EQ charge mode. get in (A).
            # "67.0", # the percent of the battery capacity which the battery charge mode turn from the float charge into the EQ charge mode.get in(%)
            # "68.0", # the battery control mode,auto EC enable flag: 0 - disable auto EC, 1 - enable auto EC

                ]
    )

)


register.check_plugin(
    name = "jetpower",
    service_name = "%s",
    discovery_function = discover_jetpower,
    check_default_parameters={},
    check_ruleset_name="jetpower",
    check_function = check_jetpower,
)