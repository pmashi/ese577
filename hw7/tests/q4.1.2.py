OK_FORMAT = True

test = {   'name': 'q4.1.2',
    'points': 7,
    'suites': [   {   'cases': [   {   'code': '>>> _a = np.asarray(A_412, dtype=float)\n>>> bool(not np.iscomplexobj(A_412) and _a.shape == (6, 6) and np.isfinite(_a).all())\nTrue',
                                       'failure_message': 'A_412 must be a finite, real 6-by-6 matrix.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> _a = np.asarray(A_412, dtype=float)\n'
                                               '>>> _a.shape == (6, 6) and (_a >= 0).all() and np.allclose(_a.sum(axis=1), np.ones(6), rtol=0, atol=1e-08)\n'
                                               'True',
                                       'failure_message': 'Attention weights must be nonnegative and each row must sum to one.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
