#!/usr/bin/env bash
current_tag=$(git tag --sort=-creatordate | sed -n 1p)
previous_tag=$(git tag --sort=-creatordate | sed -n 2p)
git shortlog "${previous_tag}.." | sed 's/^./    &/'
