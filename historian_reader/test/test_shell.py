import datetime

import nose.tools as n

import historian.shell as s

def test_session_date():
    n.assert_equal(s.session_date('2014-08-28 04:00:44.588995803+00:00'),
                   datetime.datetime(2014, 8, 28, 4, 0, 44))

def test_read_session():
def read_session(fp):
