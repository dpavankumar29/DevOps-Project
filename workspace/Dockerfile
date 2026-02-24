FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install required packages
RUN apt-get update && apt-get install -y \
    curl \
    git \
    python3 \
    python3-pip \
    nodejs \
    npm \
    sudo \
    && apt-get clean

# Install VS Code Server (code-server)
RUN curl -fsSL https://code-server.dev/install.sh | sh

# Create non-root user
RUN useradd -m coder \
    && echo "coder:coder" | chpasswd \
    && adduser coder sudo

USER coder
WORKDIR /home/coder

# Change port to 7070 (important)
EXPOSE 7070

CMD ["code-server", "--bind-addr", "0.0.0.0:7070", "--auth", "none"]