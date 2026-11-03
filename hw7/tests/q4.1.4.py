OK_FORMAT = True

test = {   'name': 'q4.1.4',
    'points': 10,
    'suites': [   {   'cases': [   {   'code': '>>> ret = True\n'
                                               ">>> for _name, _value in [('WQ_414', WQ_414), ('WK_414', WK_414)]:\n"
                                               "...     ret = (ret and (not np.iscomplexobj(_value)), _name + ' must be real.')\n"
                                               '...     _w = np.asarray(_value, dtype=float)\n'
                                               '...     ret = ret and _w.shape == (2, 3)\n'
                                               '...     ret = ret and np.isfinite(_w).all()\n'
                                               '>>> bool(ret)\n'
                                               'True',
                                       'failure_message': 'Both query and key projections must be finite, real 2-by-3 matrices.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
