import sys
import csv

import historian_reader.shell

def main():
    writer = csv.writer(sys.stdout)
    writer.writerow(('session','session_date','command_date','command'))
    try:
        for session in historian_reader.shell.historian():
            for command in session['commands']:
                command_date, command_string = command
                writer.writerow((session['session'],
                                 session['session_date'].timestamp(),
                                 command_date.timestamp(),
                                 command_string))
    except KeyboardInterrupt:
        pass
    except BrokenPipeError:
        pass
