OK_FORMAT = True

test = {   'name': 'q3.1.2',
    'points': 15,
    'suites': [   {   'cases': [   {   'code': ">>> q = TabularQ([0, 1, 2, 3], ['b', 'c'])\n"
                                               ">>> q.set(0, 'b', 5)\n"
                                               ">>> q.set(0, 'c', 10)\n"
                                               ">>> q.set(1, 'b', 2)\n"
                                               ">>> greedy_312(q, 0) == 'c' and greedy_312(q, 1) == 'b'\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
