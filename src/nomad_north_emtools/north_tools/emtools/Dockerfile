ARG IMAGE_TAG=main
ARG BASE_IMAGE=ghcr.io/fairmat-nfdi/nomad-north-desktop-base
ARG PLUGIN_NAME=nomad-north-emtools

FROM ${BASE_IMAGE}:${IMAGE_TAG} AS base

# Fix: https://github.com/hadolint/hadolint/wiki/DL4006
# Fix: https://github.com/koalaman/shellcheck/wiki/SC3014
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

# with pre-existing NB_USER="jovyan" and NB_UID=100, NB_GID=1000
ENV HOME=/home/${NB_USER}
ENV CONDA_DIR=/opt/conda

RUN apt update \
   && apt-get install --no-install-recommends -y \
        wget \
        libgl1 \
        libglu1-mesa \
        libglu1-mesa-dev \
   && rm -rf /var/lib/apt/lists/*

COPY --chown=${NB_UID}:${NB_GID} "src/nomad_north_emtools/north_tools/emtools/environment.yml" "/tmp/environment.yml"
# see nomad-north-nionswift plugins Dockerfile on how to possibly make that copy layering slimmer

# Create the named environment with packages as mentioned in the environment.yml file, clear mamba cache
# ARG env_name=emtools
RUN mamba env create -f "/tmp/environment.yml" \
    && mamba clean --all -f -y \
    && rm -rf "/tmp/environment.yml"

# Register environment as Jupyter kernel
RUN conda run -n emtools python -m ipykernel install --user --name=emtools \
    && fix-permissions "${CONDA_DIR}" \
    && fix-permissions "${HOME}"

RUN echo "\n# Automatically activate apmtools environment" >> "${HOME}/.bashrc" \
    && echo "conda activate emtools" >>"${HOME}/.bashrc" \
    && chown ${NB_UID}:${NB_GID} "${HOME}/.bashrc"

# Switch back to jovyan to avoid accidental container runs as root
USER ${NB_UID}
WORKDIR "${HOME}"
