OK_FORMAT = True

test = {   'name': 'q4.2.2',
    'points': 4,
    'suites': [   {   'cases': [   {   'code': '>>> _w = np.asarray(WV_422, dtype=float)\n'
                                               '>>> bool(not np.iscomplexobj(WV_422) and _w.ndim == 2 and (_w.shape[1] == 3) and (_w.shape[0] >= 1) and np.isfinite(_w).all())\n'
                                               'True',
                                       'failure_message': 'WV_422 must be a finite, real matrix with three columns.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
