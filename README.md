Usage:

```bash
python bidsrename bids_dir original_id new_id [--dry-run]
```

`bids_dir` is a BIDS dataset, `original_id` is the original id to change (already present in the dataset) and
`new_id` is the new id (non-existent in the dataset).

Caution: the old data are not suppressed by this script, it only copies it. Also, it does not edit the `participants.tsv` file - you have to do it manually.
