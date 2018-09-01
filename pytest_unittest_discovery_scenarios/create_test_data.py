import glob
import os
import sys


# ### `create_test_data.py`
# Use this script to generate test data from all the scenario mock ups in this
# repository. The test data is created in JSON format and stored as a type that
# our extension unit tests can consume.

# Example use:
# `> python create_test_data.py scenario_* all_scenario_data.json`

# This will create the file `all_scenario_data.json` containing the stdout and
# expected tests to find in the current folder, from each scenario_* folder 
# located in the current folder.

# Example use:
# `> python create_test_data.py /home/user/tests/scenario_one /opt/testdata/out.json`

# This will take the test scenario in a specifically named folder only, and write
# that data out to the file `/opt/testdata/out.json`.


def write_test_data(data_file_path, test_data):
    pass


def get_test_collection_stdout(scenario_dir):
    """Capture stdout from `pytest --collect-only -s --cache-clear`, convert to data."""
    return ''


def extract_test_data(scenario_dir):
    return []
    

def get_scenario_paths(path_spec):
    """Resolve the given path specification to a list of absolute paths."""
    found_paths = []
    for filename in glob.iglob(path_spec, recursive=True):
        if os.path.isdir(filename):
            print(f'Found scenario directory "{filename}"')
            found_paths.append(filename)
    return found_paths
    

def main():
    """Check arguments and start the process."""
    if len(sys.argv) != 3:
        print('Usage:')
        print()
        print('> python create_test_data.py FOLDER_SPEC OUT_FILE')
        print()
        print('   FOLDER_SPEC:   Path to the folder to create test data from,')
        print('                  can include wildcards.')
        print('   OUT_FILE:      Path to write the output file to. JSON.')
        print()
    else:
        scenario_data_paths = get_scenario_paths(sys.argv[1])
        test_data_path = os.path.realpath(sys.argv[2])
        test_data = []
        for scenario_dir in scenario_data_paths:
            scenario_data = extract_test_data(scenario_dir)
            test_data.append(scenario_data)
        write_test_data(test_data_path, test_data)
        


if __name__ == '__main__':
    main()