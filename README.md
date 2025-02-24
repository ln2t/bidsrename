Usage:

```bash
python bidsrename bids_dir original_id new_id [--dry-run]
```

`bids_dir` is a BIDS dataset, `original_id` is the original id to change (already present in the dataset) and
`new_id` is the new id (non-existent in the dataset).
Add `--dry-run` to actually skip any renaming - for verification/debugging purposes. We recommend always start with a dry-run and check that the output is consistent with what you expect.


Caution: the old data are not suppressed by this script, it only copies it. Also, it does not edit the `participants.tsv` file.
So you always have to manually delete the old data and edit the `participants.tsv` file.
