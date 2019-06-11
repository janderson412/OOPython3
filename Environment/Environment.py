import os
if __name__ == '__main__':
    # process command line parameters

    # get environment
    environment = os.environ
    env_names = environment.keys()
    env_sorted = sorted(env_names)
    for name in env_sorted:
        print('{0} = {1}'.format(name, environment[name]))
