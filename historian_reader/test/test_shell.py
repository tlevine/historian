import datetime
import os
import csv

import nose.tools as n

import historian_reader.shell as s

def test_session_date():
    n.assert_equal(s.session_date('2014-08-28 04:00:44.588995803+00:00'),
                   datetime.datetime(2014, 8, 28, 4, 0, 44))

def test_read_session():
    with open(os.path.join('historian_reader', 'test', 'fixtures', '2014-08-23 02:27:05.033008250+00:00')) as fp:
        observed = list(s.read_session(fp))

    with open(os.path.join('historian_reader', 'test', 'fixtures', '2014-08-23 02:27:05.033008250+00:00.csv')) as fp:
        expected = [(int(a),datetime.datetime.fromtimestamp(int(b)),c) \
                    for (a,b,c) in csv.reader(fp)]

    n.assert_list_equal(observed, expected)
