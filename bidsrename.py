from bids import BIDSLayout
from pathlib import Path
import shutil
import argparse
import warnings


def make_parent_dir(file_path):
    """
    Ensure that the directory for a given file path exists.
    If it does not exist, create it.

    Args:
    file_path (str): The full path to the file, including the filename.

    Example:
    ensure_directory("/path/to/my/directory/filename.txt")
    """
    Path(file_path).parents[0].mkdir(exist_ok=True, parents=True)


parser = argparse.ArgumentParser(
        description="BIDSrename: tool to rename a participant in a BIDS dataset")
parser.add_argument("bids_dir", type=str, help="BIDS root directory containing the dataset.")
parser.add_argument("original_subject_id", type=str, help="Name of the existing subject to rename (e.g. 01)")
parser.add_argument("new_subject_id", type=str, help="New subject id to assign to subject (e.g. 04)")
parser.add_argument("--dry_run", help="Option to skip actual renaming (for verification purposes).", action="store_true")

args = parser.parse_args()

bids_dir = args.bids_dir
original_subject_id = args.original_subject_id
new_subject_id = args.new_subject_id
dry_run = args.dry_run

if dry_run:
    print("Running in dry run mode, no files will be renamed.")

if original_subject_id == new_subject_id:
    raise ValueError(f"Please select different subject id.")

layout = BIDSLayout(bids_dir)
subjects = layout.get_subjects()

if new_subject_id in subjects:
    raise ValueError(f"Selected new name {new_subject_id} already present in the database!")

if original_subject_id in subjects:

    original_files = layout.get(subject=original_subject_id, return_type="filename")

    if len(original_files) == 0:
        raise ValueError("No file found to rename...")
    else:
        print(f"Found {len(original_files)} files to rename:")

    original_subject_id = "sub-" + original_subject_id
    new_subject_id = "sub-" + new_subject_id

    for file in original_files:
        new_file = file.replace(original_subject_id, new_subject_id)
        print(f"Renaming {file} to {new_file}")
        if not dry_run:
            make_parent_dir(new_file)
            shutil.copy(file, new_file)
else:
    raise ValueError(f"Subject \'{original_subject_id}\' not found in database. The existing subjects are {subjects}.")

warnings.warn("This script does NOT delete original data, please do it manually!")
warnings.warn("Don't forget to update your participants.tsv table!")