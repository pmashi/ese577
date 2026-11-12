OK_FORMAT = True

test = {   'name': 'q3.1.1',
    'points': 15,
    'suites': [   {   'cases': [   {   'code': ">>> q = TabularQ([0, 1, 2, 3], ['b', 'c'])\n"
                                               ">>> q.set(0, 'b', 5)\n"
                                               ">>> q.set(0, 'c', 10)\n"
                                               '>>> q_star = value_311(q, 0)\n'
                                               '>>> q_star == 10 and isinstance(q_star, int)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
