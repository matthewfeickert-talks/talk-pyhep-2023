#!/bin/bash

IMAGE="mambaorg/micromamba:1.4.9-bullseye-slim"

docker pull "${IMAGE}"

docker run \
    --rm \
    --volume "${PWD}":/work \
    --workdir /work \
    "${IMAGE}" \
    /bin/bash -c "\
        micromamba install \
            --yes \
            --channel conda-forge \
            conda-lock \
            git && \
        conda-lock lock \
            --micromamba \
            --file environment.yml && \
        mv conda-lock.yml binder/"
