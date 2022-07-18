#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

from cmk.gui.i18n import _

from cmk.gui.plugins.metrics import (
    check_metrics,
    metric_info,
    graph_info,
)

metric_info['system_status'] = {
	'title': _('System status'),
	'unit': '',
	'color': '31/b',
}

metric_info['system_voltage'] = {
	'title': _('Voltege Output'),
	'unit': 'v',
	'color': '51/a',
}

metric_info['system_current_load'] = {
	'title': _('System current load'),
	'unit': 'a',
	'color': '14/a',
}

metric_info['system_ac'] = {
	'title': _('System input AC'),
	'unit': 'v',
	'color': '24/a',
}



