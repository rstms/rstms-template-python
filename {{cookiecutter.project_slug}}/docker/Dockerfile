ARG BASE_IMAGE
ARG USER
ARG CMD
FROM ${BASE_IMAGE}
RUN addgroup ${USER} && adduser ${USER} ${USER}
COPY entrypoint /entrypoint
ENTRYPOINT ["/entrypoint"]
COPY VERSION /VERSION
USER ${USER}
WORKDIR /home/${USER}
COPY *.whl .
RUN sh -c 'pip install *.whl'
CMD ${CMD}
