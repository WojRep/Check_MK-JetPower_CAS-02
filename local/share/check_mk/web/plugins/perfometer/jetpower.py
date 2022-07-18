#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

from cmk.gui.plugins.views.perfometers import (
    perfometer_linear,
)

def perfometer_jetpower(row, check_command, perf_data):

    PERF = {
        'system_current_load': {'type': 'linear', 'max': 15, 'color': 'red'},
    }

    debug_file = open("/tmp/perfometer.log", "a")
    _ = str(perf_data)
    _ = '#################\n'
    debug_file.write(str(_))
    debug_file.close()


    for perf in perf_data:
        perf = list(perf)
        if PERF.get(perf[0]):
#        if (name, value, _1, _2, _3, _4, _5 = perf):
            name, value, xxx, warm, crit, _min, _max = perf
            perf_def = PERF[name]
            if perf_def['type'] == 'linear':
                perc_value = value * 100 / perf_def['max']
                return u"%s" % str(value), perfometer_linear(perc_value, perf_def['color'])

perfometers['check_mk-jetpower'] = perfometer_jetpower
