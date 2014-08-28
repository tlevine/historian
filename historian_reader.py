import os

HISTORY = os.path.join(os.path.expanduser('~'), 'history', 'shell')
DATESTAMP_LENGTH = len('#1409184772')

def historian(directory = HISTORY, skip = []):
    '''
    directory: Directory containing the shell history
    already_read: Names of history files to skip (because they have
        already been processed)
    '''
    sessions = sorted(set(os.listdir(HISTORY)).difference(skip))
    for session in sessions:
        result = {
            'session': session,
            'session_date': session_date(session),
        }
        with open(session, 'r') as fp:
            result['commands'] = list(read_session(fp))
        yield result

def session_date(session:str):
    '''
    >>> session_date('2014-08-28 04:00:44.588995803+00:00')
    datetime.datetime(2014, 8, 28, 4, 0, 44)
    '''
    return datetime.datetime.strptime(session.split('.')[0], '%Y-%m-%d %H:%M:%S')

def split_commands(fp):
    'This doesn\'t handle comments correctly.'
    s = shlex.shlex(instream = fp, posix = True)
    s.whitespace_split = True
    s.commenters = ''

    for token in s:
        if len(token) == DATESTAMP_LENGTH:
            try:
                yield command_date, tokens
            except NameError:
                pass
            command_date = datetime.datetime.fromtimestamp(int(token[1:]))
            tokens = []
        else:
            tokens.append(token)

def read_session(fp):
    for command_date, tokens in split_commands(fp):

