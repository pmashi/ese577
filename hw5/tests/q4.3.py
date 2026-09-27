OK_FORMAT = True

test = {   'name': 'q4.3',
    'points': 10,
    'suites': [   {   'cases': [   {   'code': '>>> y = np.array([[1, 0, 1, 0]]).T\n'
                                               '>>> Y = np.hstack([1 - y, y])\n'
                                               '>>> ypred = np.array([[0.7, 0.3, 0.99, 0.99]]).T\n'
                                               '>>> Ypred = np.hstack([1 - ypred, ypred])\n'
                                               '>>> nll = NLLM_43()\n'
                                               '>>> ans = nll.forward(Ypred, Y)\n'
                                               '>>> expected = np.array([[5.328570409719057]])\n'
                                               '>>> ans.shape == expected.shape and np.allclose(ans, expected)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> y = np.array([[1, 0, 1, 0]]).T\n'
                                               '>>> Y = np.hstack([1 - y, y])\n'
                                               '>>> ypred = np.array([[0.7, 0.3, 0.99, 0.99]]).T\n'
                                               '>>> Ypred = np.hstack([1 - ypred, ypred])\n'
                                               '>>> nll = NLLM_43()\n'
                                               '>>> _ = nll.forward(Ypred, Y)\n'
                                               '>>> ans = nll.backward()\n'
                                               '>>> expected = np.array([[0.3, -0.3], [-0.3, 0.3], [0.01, -0.01], [-0.99, 0.99]])\n'
                                               '>>> np.allclose(ans, expected)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
