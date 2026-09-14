OK_FORMAT = True

test = {   'name': 'q4.2',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> dsigmoid_dz_42_str = inspect.getsource(dsigmoid_dz_42)\n'
                                               ">>> re.search('\\\\bz\\\\b', dsigmoid_dz_42_str) is None and re.search('\\\\bnp\\\\.e\\\\b', dsigmoid_dz_42_str) is None\n"
                                               'True',
                                       'failure_message': "Your function should not use np.e or z. (If you have 'np.e' or 'z' in a comment, please also remove those).",
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
