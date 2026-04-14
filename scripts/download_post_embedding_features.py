#!/usr/bin/env python3
"""
Download post-level *features.npy files from a Hugging Face dataset repo into data_post_embedding/.

Usage:
  export HF_POST_EMBEDDING_REPO=YOUR_USERNAME/your-dataset-name
  python scripts/download_post_embedding_features.py

Requires: pip install huggingface_hub
Optional: huggingface-cli login   # or set HF_TOKEN
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path

REPO_ENV = "HF_POST_EMBEDDING_REPO"
# Primary dataset (browser): https://huggingface.co/datasets/sijiey/Urban-Comfort-Potential
DEFAULT_REPO = "sijiey/Urban-Comfort-Potential"


def list_feature_npys(repo_id: str, token: str | bool | None) -> list[str]:
    """Paths in the dataset repo whose basename ends with features.npy."""
    from huggingface_hub import HfApi

    api = HfApi(token=token)
    files = api.list_repo_files(repo_id, repo_type="dataset")
    out = []
    for f in files:
        if Path(f).name.endswith("features.npy"):
            out.append(f)
    return sorted(set(out))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo",
        default=os.environ.get(REPO_ENV, DEFAULT_REPO),
        help=f"Hugging Face dataset repo id (default: env {REPO_ENV} or {DEFAULT_REPO})",
    )
    parser.add_argument(
        "--dest",
        type=Path,
        default=Path("data_post_embedding"),
        help="Local folder (created if missing)",
    )
    parser.add_argument(
        "--token",
        default=None,
        help="HF token (default: huggingface_hub cached login / HF_TOKEN)",
    )
    args = parser.parse_args()

    token = args.token if args.token else True

    try:
        names = list_feature_npys(args.repo, token)
    except Exception as e:
        raise SystemExit(
            f"Could not list files in dataset {args.repo!r}. "
            f"Create the repo on huggingface.co/datasets and upload files first. ({e})"
        ) from e

    if not names:
        raise SystemExit(
            f"No *features.npy files found in {args.repo}. "
            "Upload with: python scripts/upload_post_embedding_features.py"
        )

    args.dest.mkdir(parents=True, exist_ok=True)

    from huggingface_hub import hf_hub_download

    print(f"Repo: {args.repo}  →  {args.dest.resolve()}")
    for rel in names:
        hf_hub_download(
            repo_id=args.repo,
            filename=rel,
            repo_type="dataset",
            local_dir=str(args.dest),
            token=token,
        )
        print(f"  OK  {Path(rel).name}")

    print(f"Done. {len(names)} file(s).")


if __name__ == "__main__":
    main()
