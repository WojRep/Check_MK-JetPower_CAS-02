#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

from cmk.gui.plugins.metrics import perfometer_info

perfometer_info.append({
#                    "type": "logarithmic",
                    "type": "linear",
                    "metric": "system_current_load",
#                    "half_value": 1.0,
#                    "exponent": 2.0,
		     "total": 2.0,
})

