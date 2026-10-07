# CITS2006 lab container: Linux tools that need root (ACLs, users) plus a matched YARA CLI and Python binding.
# Build:  docker build -t cits2006-env "https://github.com/uwacyber/cits2006.git#live:cits2006-labs/env"
# Run:    docker run --rm -it -v "$PWD:/work" cits2006-env
FROM debian:13-slim
RUN apt-get update && apt-get install -y --no-install-recommends \
        acl sudo python3 python3-yara yara curl ca-certificates nano less procps \
        iproute2 iputils-ping bind9-dnsutils file xxd \
    && rm -rf /var/lib/apt/lists/*
RUN useradd -m -s /bin/bash student && echo 'student ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/student
# WORKDIR creates /work owned by root; hand it to student so it is writable when no folder is mounted
RUN install -d -o student -g student /work
USER student
WORKDIR /work
CMD ["bash"]
