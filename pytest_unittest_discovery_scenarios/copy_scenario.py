import os
import shutil
import sys
import tarfile

NEVER_COPY_DIRNAMES = [
    ".pytest_cache",
    "__pycache__",
    ".venv-pytest_37",
    ".venv-pytest_36",
    ".git",
]


def compress_scenario(scenario_name, scenario_folder):
    tarfile_folder, _ = os.path.split(scenario_folder)
    tarfile_path = os.path.join(tarfile_folder, f'{scenario_name}.tar.gz')
    archive = tarfile.open(tarfile_path, 'w:gz')
    archive.add(scenario_folder, arcname=scenario_name)


def do_not_copy(src, names):
    ignore_names = []
    for copy_path in names:
        _, src_name = os.path.split(copy_path)
        if src_name in NEVER_COPY_DIRNAMES:
            ignore_names.append(src_name)
    return ignore_names


def create_scenario(scenario_name, dir_to_copy):
    copy_to_root, _ = os.path.split(dir_to_copy)
    copy_to_path = os.path.join(copy_to_root, scenario_name)
    shutil.copytree(
        dir_to_copy, copy_to_path, symlinks=False,
        ignore=do_not_copy)
    compress_scenario(scenario_name, copy_to_path)
    shutil.rmtree(copy_to_path)


def main():
    if len(sys.argv) != 3:
        print("Try again, but give me a scenario name and a dir name.")
    else:
        scenario_name = sys.argv[1]
        src_folder = os.path.realpath(sys.argv[2])
        create_scenario(scenario_name, src_folder)


if __name__ == "__main__":
    main()
