FROM continuumio/miniconda3:4.10.3-alpine

# Define default parameters
USER root
WORKDIR /geometry/
ENV PATH=/opt/conda/bin:$PATH
ENV LD_LIBRARY_PATH=/usr/local/lib:${LD_LIBRARY_PATH}

# Install dependencies
COPY environment.yml /geometry/
RUN conda config --set notify_outdated_conda false && \
    conda config --set channel_priority strict && \
    conda env update --prune && \
    conda clean --all --yes --force-pkgs-dirs && \
    find /opt/conda/ -follow -type f -name '*.a' -delete && \
    find /opt/conda/ -follow -type f -name '*.pyc' -delete && \
    find /opt/conda/ -follow -type f -name '*.js.map' -delete

# Copy Python scripts
COPY bin    /geometry/bin
