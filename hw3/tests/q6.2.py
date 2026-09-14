OK_FORMAT = True

test = {   'name': 'q6.2',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> ans = d_sigmoid_62(np.array([[71.0]]))\n>>> np.shape(ans) == (1, 1) and np.array(ans[0, 0] == 0.0).item()\nTrue',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> ans = d_sigmoid_62(np.array([[-23.0]]))\n>>> np.shape(ans) == (1, 1) and np.isclose(ans[0, 0], 1.0261879629595766e-10).item()\nTrue',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> ans = d_sigmoid_62(np.array([[71, -23.0]]))\n>>> np.shape(ans) == (1, 2) and np.allclose(ans, np.array([[0.0, 1.0261879629595766e-10]]))\nTrue',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> X1 = np.array([[1, 2, 3, 9, 10]]).T\n'
                                               '>>> y1 = np.array([[1, 1, 1, 0, 0]]).T\n'
                                               '>>> th1, th10 = (np.array([[-0.31202807]]), np.array([[1.834]]))\n'
                                               '>>> X2 = np.array([[2, 3, 9, 12], [5, 2, 6, 5]]).T\n'
                                               '>>> y2 = np.array([[1, 0, 1, 0]]).T\n'
                                               '>>> th2, th20 = (np.array([[-3.0, 15.0]]).T, np.array([[2.0]]))\n'
                                               '>>> ans = d_nll_loss_th_62(X2[0:1, :], y2[0:1, :], th2, th20)\n'
                                               '>>> ans.shape == (1, 2) and np.allclose(ans, np.array([[0.0, 0.0]]))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> X1 = np.array([[1, 2, 3, 9, 10]]).T\n'
                                               '>>> y1 = np.array([[1, 1, 1, 0, 0]]).T\n'
                                               '>>> th1, th10 = (np.array([[-0.31202807]]), np.array([[1.834]]))\n'
                                               '>>> X2 = np.array([[2, 3, 9, 12], [5, 2, 6, 5]]).T\n'
                                               '>>> y2 = np.array([[1, 0, 1, 0]]).T\n'
                                               '>>> th2, th20 = (np.array([[-3.0, 15.0]]).T, np.array([[2.0]]))\n'
                                               '>>> ans = d_nll_loss_th_62(X2, y2, th2, th20)\n'
                                               '>>> ans.shape == X2.shape and np.allclose(ans, np.array([[0.0, 0.0], [3.0, 2.0], [0.0, 0.0], [12.0, 5.0]]))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> X1 = np.array([[1, 2, 3, 9, 10]]).T\n'
                                               '>>> y1 = np.array([[1, 1, 1, 0, 0]]).T\n'
                                               '>>> th1, th10 = (np.array([[-0.31202807]]), np.array([[1.834]]))\n'
                                               '>>> X2 = np.array([[2, 3, 9, 12], [5, 2, 6, 5]]).T\n'
                                               '>>> y2 = np.array([[1, 0, 1, 0]]).T\n'
                                               '>>> th2, th20 = (np.array([[-3.0, 15.0]]).T, np.array([[2.0]]))\n'
                                               '>>> ans = d_nll_loss_th0_62(X2[0:1, :], y2[0:1, :], th2, th20)\n'
                                               '>>> ans.shape == (1, 1) and np.isclose(ans, np.array([[0.0]])).item()\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> X1 = np.array([[1, 2, 3, 9, 10]]).T\n'
                                               '>>> y1 = np.array([[1, 1, 1, 0, 0]]).T\n'
                                               '>>> th1, th10 = (np.array([[-0.31202807]]), np.array([[1.834]]))\n'
                                               '>>> X2 = np.array([[2, 3, 9, 12], [5, 2, 6, 5]]).T\n'
                                               '>>> y2 = np.array([[1, 0, 1, 0]]).T\n'
                                               '>>> th2, th20 = (np.array([[-3.0, 15.0]]).T, np.array([[2.0]]))\n'
                                               '>>> ans = d_nll_loss_th0_62(X2, y2, th2, th20)\n'
                                               '>>> ans.shape == (4, 1) and np.allclose(ans, np.array([[0.0, 1.0, 0.0, 1.0]]).T)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> X1 = np.array([[1, 2, 3, 9, 10]]).T\n'
                                               '>>> y1 = np.array([[1, 1, 1, 0, 0]]).T\n'
                                               '>>> th1, th10 = (np.array([[-0.31202807]]), np.array([[1.834]]))\n'
                                               '>>> X2 = np.array([[2, 3, 9, 12], [5, 2, 6, 5]]).T\n'
                                               '>>> y2 = np.array([[1, 0, 1, 0]]).T\n'
                                               '>>> th2, th20 = (np.array([[-3.0, 15.0]]).T, np.array([[2.0]]))\n'
                                               '>>> ans = d_llc_obj_th_62(X2[0:1, :], y2[0:1, :], th2, th20, 0.01)\n'
                                               '>>> ans.shape == (2, 1) and np.allclose(ans, np.array([[-0.06, 0.3]]).T)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> X1 = np.array([[1, 2, 3, 9, 10]]).T\n'
                                               '>>> y1 = np.array([[1, 1, 1, 0, 0]]).T\n'
                                               '>>> th1, th10 = (np.array([[-0.31202807]]), np.array([[1.834]]))\n'
                                               '>>> X2 = np.array([[2, 3, 9, 12], [5, 2, 6, 5]]).T\n'
                                               '>>> y2 = np.array([[1, 0, 1, 0]]).T\n'
                                               '>>> th2, th20 = (np.array([[-3.0, 15.0]]).T, np.array([[2.0]]))\n'
                                               '>>> ans = d_llc_obj_th_62(X2, y2, th2, th20, 0.01)\n'
                                               '>>> ans.shape == (2, 1) and np.allclose(ans, np.array([[3.69, 2.05]]).T)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> X1 = np.array([[1, 2, 3, 9, 10]]).T\n'
                                               '>>> y1 = np.array([[1, 1, 1, 0, 0]]).T\n'
                                               '>>> th1, th10 = (np.array([[-0.31202807]]), np.array([[1.834]]))\n'
                                               '>>> X2 = np.array([[2, 3, 9, 12], [5, 2, 6, 5]]).T\n'
                                               '>>> y2 = np.array([[1, 0, 1, 0]]).T\n'
                                               '>>> th2, th20 = (np.array([[-3.0, 15.0]]).T, np.array([[2.0]]))\n'
                                               '>>> ans = d_llc_obj_th0_62(X2[0:1, :], y2[0:1, :], th2, th20, 0.01)\n'
                                               '>>> ans.shape == (1, 1) and np.isclose(ans, np.array([[0.0]])).item()\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> X1 = np.array([[1, 2, 3, 9, 10]]).T\n'
                                               '>>> y1 = np.array([[1, 1, 1, 0, 0]]).T\n'
                                               '>>> th1, th10 = (np.array([[-0.31202807]]), np.array([[1.834]]))\n'
                                               '>>> X2 = np.array([[2, 3, 9, 12], [5, 2, 6, 5]]).T\n'
                                               '>>> y2 = np.array([[1, 0, 1, 0]]).T\n'
                                               '>>> th2, th20 = (np.array([[-3.0, 15.0]]).T, np.array([[2.0]]))\n'
                                               '>>> ans = d_llc_obj_th0_62(X2, y2, th2, th20, 0.01)\n'
                                               '>>> ans.shape == (1, 1) and np.isclose(ans, np.array([[0.5]])).item()\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> X1 = np.array([[1, 2, 3, 9, 10]]).T\n'
                                               '>>> y1 = np.array([[1, 1, 1, 0, 0]]).T\n'
                                               '>>> th1, th10 = (np.array([[-0.31202807]]), np.array([[1.834]]))\n'
                                               '>>> X2 = np.array([[2, 3, 9, 12], [5, 2, 6, 5]]).T\n'
                                               '>>> y2 = np.array([[1, 0, 1, 0]]).T\n'
                                               '>>> th2, th20 = (np.array([[-3.0, 15.0]]).T, np.array([[2.0]]))\n'
                                               '>>> ans = llc_obj_grad_62(X2, y2, th2, th20, 0.01)\n'
                                               '>>> ans.shape == (3, 1) and np.allclose(ans, np.array([[3.69, 2.05, 0.5]]).T)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> X1 = np.array([[1, 2, 3, 9, 10]]).T\n'
                                               '>>> y1 = np.array([[1, 1, 1, 0, 0]]).T\n'
                                               '>>> th1, th10 = (np.array([[-0.31202807]]), np.array([[1.834]]))\n'
                                               '>>> X2 = np.array([[2, 3, 9, 12], [5, 2, 6, 5]]).T\n'
                                               '>>> y2 = np.array([[1, 0, 1, 0]]).T\n'
                                               '>>> th2, th20 = (np.array([[-3.0, 15.0]]).T, np.array([[2.0]]))\n'
                                               '>>> ans = llc_obj_grad_62(X2[0:1, :], y2[0:1, :], th2, th20, 0.01)\n'
                                               '>>> ans.shape == (3, 1) and np.allclose(ans, np.array([[-0.06, 0.3, 0.0]]).T)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
