#!/usr/bin/env python3
"""
Upload every *features.npy file under data_post_embedding/ to a Hugging Face dataset repo.

Files matched: name ends with 'features.npy' (e.g. dataset_post_resnet_features.npy,
dataset_post_st_caption_features.npy).

Usage:
  huggingface-cli login
  export HF_POST_EMBEDDING_REPO=YOUR_USERNAME/your-dataset-name
  python scripts/upload_post_embedding_features.py

Create the (empty) dataset on https://huggingface.co/new-dataset first, or pass --create-repo.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path

REPO_ENV = "HF_POST_EMBEDDING_REPO"
DEFAULT_REPO = "sijiey/Urban-Comfort-Potential"


def iter_feature_files(root: Path) -> list[Path]:
    out = []
    for p in sorted(root.glob("*.npy")):
        if p.name.endswith("features.npy"):
            out.append(p)
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo",
        default=os.environ.get(REPO_ENV, DEFAULT_REPO),
        help=f"HF dataset repo id (default: env {REPO_ENV})",
    )
    parser.add_argument(
        "--src",
        type=Path,
        default=Path("data_post_embedding"),
        help="Folder containing *.npy",
    )
    parser.add_argument(
        "--create-repo",
        action="store_true",
        help="Create the dataset repo if it does not exist (needs token with write access)",
    )
    parser.add_argument(
        "--token",
        default=None,
        help="HF token (optional if already logged in)",
    )
    args = parser.parse_args()

    files = iter_feature_files(args.src)
    if not files:
        raise SystemExit(
            f"No *features.npy files under {args.src.resolve()}. Nothing to upload."
        )

    from huggingface_hub import HfApi

    token = args.token if args.token else True
    api = HfApi(token=token)

    if args.create_repo:
        api.create_repo(
            repo_id=args.repo,
            repo_type="dataset",
            exist_ok=True,
            token=token,
        )

    print(f"Uploading to dataset {args.repo} ({len(files)} files)")
    for fp in files:
        # Flat layout in repo: filename at root (simplest for download script)
        api.upload_file(
            path_or_fileobj=str(fp),
            path_in_repo=fp.name,
            repo_id=args.repo,
            repo_type="dataset",
            token=token,
            commit_message=f"Add {fp.name}",
        )
        print(f"  OK  {fp.name}")

    print("Done. Set HF_POST_EMBEDDING_REPO for collaborators and run download_post_embedding_features.py")


if __name__ == "__main__":
    main()
