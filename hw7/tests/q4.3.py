OK_FORMAT = True

test = {   'name': 'q4.3',
    'points': 6,
    'suites': [   {   'cases': [   {   'code': '>>> _s = np.asarray(scores_413, dtype=float)\n'
                                               '>>> bool(not np.iscomplexobj(scores_413) and _s.shape == (6, 6) and (not np.isnan(_s).any()) and (not np.isposinf(_s).any()) and '
                                               'np.isfinite(_s).any(axis=1).all())\n'
                                               'True',
                                       'failure_message': 'Check score shape, numeric values, and whether every row has a visible key.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
