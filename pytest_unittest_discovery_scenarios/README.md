# README
## PyTest Test Data for Vscode-Python 

This repo is to create test data for unit testing pytest within the 
VSCode-Python extension's codebase.

## Directory Summary

Each directory underneath this that is named scenario_* represents a single
scenario we wish to test our pytest unit test discovery routine with. Within
each of these folders, a mock-up of a specific source repository with various
layouts used to test the abilites of our test discovery routines.

## Scripts Summary

### `copy_scenario.py`
Use this script to copy a new scenario folder into a tar file. Use this while
iterating on the construction of new scenario mock ups. (Until I turned this
entire effort into a repository, I was storing each scenario as an archive
on my local machine).

Example use:
`> python copy_scenario.py scenario_multiple_modules_in_root_folder /home/user/tests/scenario_base`

This will create a tar file containing only the mock-up sources with path:
`/home/user/tests/scenario_multiple_modules_in_root_folder.tar.gz`

### `create_test_data.py`
Use this script to generate test data from all the scenario mock ups in this
repository. The test data is created in JSON format and stored as a type that
our extension unit tests can consume.

Example use:
`> python create_test_data.py scenario_* all_scenario_data.json`

This will create the file `all_scenario_data.json` containing the stdout and
expected tests to find in the current folder, from each scenario_* folder 
located in the current folder.

Example use:
`> python create_test_data.py /home/user/tests/scenario_one /opt/testdata/out.json`

This will take the test scenario in a specifically named folder only, and write
that data out to the file `/opt/testdata/out.json`.

