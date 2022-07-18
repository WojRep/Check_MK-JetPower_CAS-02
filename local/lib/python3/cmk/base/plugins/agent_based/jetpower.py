#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-
#
from .agent_based_api.v1 import *

from .agent_based_api.v1.type_defs import *

from .utils import (
    temperature,
)

from typing import Dict, List

from cmk.utils import debug
from pprint import pprint

#####################################################
#####################################################
##                                                 ##
##      ___      _  ______                         ##
##     |_  |    | | | ___ \                        ##
##       | | ___| |_| |_/ /____      _____ _ __    ##
##       | |/ _ \ __|  __/ _ \ \ /\ / / _ \ '__|   ##
##   /\__/ /  __/ |_| | | (_) \ V  V /  __/ |      ##
##   \____/ \___|\__\_|  \___/ \_/\_/ \___|_|      ##
##                                                 ##
##                                                 ##
##         _____ _        _                        ##
##        / ____| |      | |                       ##
##       | (___ | |_ __ _| |_ _   _ ___            ##
##        \___ \| __/ _` | __| | | / __|           ##
##        ____) | || (_| | |_| |_| \__ \           ##
##       |_____/ \__\__,_|\__|\__,_|___/           ##
##                                                 ##
##                                                 ##
#####################################################
#####################################################



#JETPOWER_TEMP_CHECK_DEFAULT_PARAMETERS = {
#    "levels": (50, 75),
#    "lower_levels": (5,0),
#}

SYSTEM_STATUS_NAME = {
	"1": "normal",
	"2": "minnor alarm",
        "3": "major alarm",
}

alarm_name = {
	"0": "normal",
	"1": "Alarm",
}

NAME="jetpower"
SNMP_BASE = ".1.3.6.1.4.1.38747.1"
SNMP_DETECT = startswith(".1.3.6.1.2.1.1.2.0", ".1.3.6.1.4.1.38747")

OIDs = {
'0': {'id': 'model_name', 'oid': '2.0', 'name': "Model", 'do_metric': False, 'unit': None, },
'1': {'id': 'firmware_version', 'oid': '3.0', 'name': 'Firmware', 'do_metric': False, 'unit': None, },
'2': {'id': 'site_name', 'oid': '4.0', 'name': 'Site name', 'do_metric':False, 'unit': None, },
'3': {'id': 'system_status', 'oid': '5.0', 'name': 'System status', 'do_metric': True, 'unit':'', 'divider': 1,  },
'4': {'id': 'system_voltage', 'oid': '6.0', 'name': 'Voltage', 'do_metric': True, 'unit': 'v', 'divider': 1000, },
'5': {'id': 'system_current_load', 'oid': '7.0', 'name': 'Current load', 'do_metric': True, 'unit': 'a', 'divider': 1000, },
'6': {'id': 'system_ac', 'oid': '8.0', 'name': 'AC voltage', 'do_metric': True, 'unit': 'v',  'divider': 1000,  },
}

#            ["9.0",],  # Battery number
#            ["11.0",], # Battery current: <0 - discharge, >0 - charge battery
#            ["12.0",], # Battery capacity in %
#            ["13.0",], # Status of battery work: 1 float charge, 2 - equalize charge
#            ["14.0",], # Rectifiers numbers (sum)
#            ["15.0",], # Rectifiers communication agent status: 1 - normal, 2 - interupt
#            ["16.0",], # Rectifiers Output Voltage
#            ["17.0",], # Rectifiers Output Current
#            ["18.0",], # Rectifiers Output Current limit
#            ["19.0",], # Rectifiers Input Voltage
#            ["20.0",], # Rectifiers Status: 0 - shutdown, 1 - power on
#            ["21.0",], # Rectifiers PugIn OK: 0 - normal, 1 - alarm
#            ["22.0",], # HVSD - Over Voltage: 0 - normal, 1 - alarm
#            ["23.0",], # Rectifiers Output status: 0 - normal, 1 -alarm
#            ["24.0",], # Rectifiers Input Over Voltage: 0 - normal, 1 - alarm
#            ["25.0",], # Rectifiers Input Under Voltage: 0 - normal, 1 - alarm
#            ["26.0",], # FAN status: 0 - normal, 1 - alarm
#            ["31.0",], # Status of communications between rectifiers: 0 - normal, 1 - unsuccessful
#            ["32.0",], # DCDC eeprom status: 0 - normal, 1 - fault
#            ["33.0",], # the output power is whtaher derated by the ac voltage or not: 0 - normal, 1 - alarm
#            ["34.0",], # the output power is whther derated by the temperature or not: 0 - normal, 1 - alarm
#            ["35.0",], # the status of the rectifier current shared with other rectifier whether ok or not: 0 - normal, 1 - alarm
#            ["36.0",], # PFC eeprom status: 0 - normal, 1 - fault
#            ["37.0",], # the status of the communication between the recitifiers and the monitor: 0 - normal, 1 - alarm
#            ["38.0",], # whether the AC voltage is normal or not: 0 - normal, 1 - out of the range
#            ["39.0",], # whether the output of the rectifier is normal or not: 0 - normal, 1 - alarm
#            ["40.0",], # whether the current of the battery is higher than the standard current which set up: 0 - normal, 1 - alarm
#            ["41.0",], # whether the temperature of the battery is normal or not: 0 - normal, 1 - alarm
#            ["42.0",], # the fuse of the battery loop: 0 - well, 1 - broken
#            ["43.0",], # the number of the load in the system
#            ["44.0",], # the fuse of the load loop: 0 - well, 1 - broken
#            ["45.0",], # BLVD --the battery low voltage disconnected: 0 - connected, 1 - disconnected
#            ["46.0",], # The digital input status of the DI port,0x01 indicates DI0 and 0x02 indicates DI1, and so on
#            ["47.0",], # The sum of active alarms
	    # ["56.0",], # the float voltage of the battery,get in V.
            # ["57.0",], # the EQ voltage of the battery,get in V
            # ["58.0",], # the maxinum of the battery current which make alarm , get in (A)
            # ["59.0",], # LLVD the voltage which the power system unload  get in V
            # ["60.0",], # BLVD--the protected voltage which the power system unload the battery   get in V
            # ["61.0",], # the limit current of the battery in EQ charge mode
            # ["62.0",], # the period of the next EQ charge time
            # ["63.0",], # the battery temperature which make alarm. get in Celsius degree
            # ["64.0",], # the capacity of the battery in the power system. get in Ah
            # ["65.0",], # the in all time of the battery in EQ charge mode. get in minute.
            # ["66.0",], # the total time of the stable current in EQ charge mode. get in (A).
            # ["67.0",], # the percent of the battery capacity which the battery charge mode turn from the float charge into the EQ charge mode.get in(%)
            # ["68.0",], # the battery control mode,auto EC enable flag: 0 - disable auto EC, 1 - enable auto EC


def _isFloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def _isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def parse_jetpower(string_table):
    param_list = {}
    parameters = string_table[0]
    for n in range(len(parameters)):
        name = OIDs[str(n)].get('name')
        do_metric = OIDs[str(n)].get('do_metric') if OIDs[str(n)].get('do_metric') else ''
        divider =  OIDs[str(n)].get('divider') if OIDs[str(n)].get('divider') else 1

        if _isInt(parameters[n]) and divider == 1:
            value = int(parameters[n])

        elif _isFloat(parameters[n]):
            value = float(parameters[n]) / divider 

        else:
            value = str(parameters[n])
            if (value is None) or (value == ''):
                value = chr(216)

        param_list.update(
		{str(OIDs[str(n)]['id']): {
		    'value': value, 
		    'name': name, 
		    'do_metric': do_metric,
		}})
    return param_list


def discover_jetpower(section):
#    if len(section) == 0:
#        return
    yield Service(item="JetPower Info")
    yield Service(item="JetPower Status")


def check_jetpower(item, params, section):
    if not section:
        yield Result(state=State.UNKNOWN, summary="No data")
        return

    if item == "JetPower Info":
        model_name = section['model_name']['value']
        firmware_version = section['firmware_version']['value']
        site_name = section['site_name']['value']

        if (model_name == "CAS-02") and (firmware_version < 66):
            yield Result(state=State.CRIT, summary=f"Upgrade firmware !!! - Your firmware: {firmware_version}")
            return
        else:
            yield Result(state=State.OK, summary=f"Model: {model_name}, Firmware: {firmware_version}, Site name: {site_name}")

        return

    #
    #
    if item == "JetPower Status":
        system_status = section['system_status']['value']
        system_voltage = section['system_voltage']['value']
        system_current_load = section['system_current_load']['value']
        system_ac = section['system_ac']['value']

        system_voltage = float("{:.1f}".format(system_voltage))
        system_current_load = float("{:.2f}".format(system_current_load))
        system_ac = float("{:.2f}".format(system_ac))

        summary = f"Status: {SYSTEM_STATUS_NAME.get(str(system_status))}, AC: {system_ac}"
        summary = summary + f"V, Voltage: {system_voltage}V, Current load: {system_current_load}A."

        if system_status == 1:
            state=State.OK
        elif system_status == 2:
            state=State.WARRNING
        elif system_status == 3:
            state=State.CRIT
        else:
            state=State.UNKNOWN
        yield Result(state=state, summary=summary)

        yield Metric('system_status', system_status)
        yield Metric('system_voltage', system_voltage)
        yield Metric('system_current_load', system_current_load)
        yield Metric('system_ac', system_ac)
        return
    yield Result(state=State.UNKNOWN, summary="No item or data")
    return




register.snmp_section(
    name=NAME,
    fetch = SNMPTree(
        base = SNMP_BASE,
        oids = [ oid['oid'] for _, oid in OIDs.items()],
    ),
    detect = SNMP_DETECT,
    parse_function = parse_jetpower,
)


register.check_plugin(
    name = NAME,
    sections=[NAME],
    service_name = "%s",
    discovery_function = discover_jetpower,
    check_default_parameters={},
    check_ruleset_name=NAME,
    check_function = check_jetpower,
)

#####################################################
#####################################################
##                                                 ##
##      ___      _  ______                         ##
##     |_  |    | | | ___ \                        ##
##       | | ___| |_| |_/ /____      _____ _ __    ##
##       | |/ _ \ __|  __/ _ \ \ /\ / / _ \ '__|   ##
##   /\__/ /  __/ |_| | | (_) \ V  V /  __/ |      ##
##   \____/ \___|\__\_|  \___/ \_/\_/ \___|_|      ##
##                                                 ##
##                                                 ##
##            _____                                ##
##           |_   _|                               ##
##             | | ___ _ __ ___  _ __              ##
##             | |/ _ \ '_ ` _ \| '_ \             ##
##             | |  __/ | | | | | |_) |            ##
##             \_/\___|_| |_| |_| .__/             ##
##                              | |                ##
##                              |_|                ##
##                                                 ##
#####################################################
#####################################################

ALARM = {
'0': 'Ambient temp. too HIGH',
'1': 'Ambient temp. too LOWER',
'2': 'Rectifiers PFC temp too HIGH',
'3': 'Rectifiers DC-DC temp too HIGH',
}


def discover_jetpower_temp(section):
    if (not section[0]) or (section[0] == None) or (section[0] == ""):
        return
    yield Service(item="JetPower Temp")


def check_jetpower_temp(item, params, section):
    if not section:
        yield Result(state=State.UNKNOWN, summary="No data")
        return

    if item and section[0] :
        alarms=section[0]
        state=State.OK

        for n in range(len(alarms)):
            alarm_value = int(alarms[n])
            if alarm_value == 1:
                summary = ALARM.get(str(n))
                state = State.CRIT
                yield Result(state=state, summary=summary)

        if state == State.OK:
            summary = f'Temperature is OK.'
            yield Result(state=state, summary=summary)    
        return

    else:
        yield Result(state = State.UNKNOWN, summary = "No correct data")

register.snmp_section(
    name=NAME + "_temp",
    fetch = SNMPTree(
	base = SNMP_BASE,
	oids = [
            "27.0", # Ambient Over temperature: 0 - normal, 1 - alarm
            "28.0", # Ambient Under temperature: 0 - normal, 1 - alarm
            "29.0", # Rectifiers PFC temperature: 0 - normal, 1 - alarm too hight
            "30.0", # Rectifiers DHDH temperature: 0 - normal, 1 - alarm too hight
	],
    ),
    detect = SNMP_DETECT,
)

register.check_plugin(
    name = NAME + "_temp",
    sections=[NAME+"_temp"],
    service_name = "%s",
    discovery_function = discover_jetpower_temp,
    check_default_parameters={},
    check_ruleset_name='',
    check_function = check_jetpower_temp,
)

