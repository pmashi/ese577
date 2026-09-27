OK_FORMAT = True

test = {   'name': 'q2.1.1',
    'points': 4,
    'suites': [   {   'cases': [   {   'code': '>>> z = np.array([[-2, -1, 0, 1, 2]]).T\n>>> isinstance(dReLU_dz_211(z), np.ndarray) and dReLU_dz_211(z).shape == (5, 1)\nTrue',
                                       'failure_message': 'Does not return a numpy column vector of the right shape.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
