FROM nikolaik/python-nodejs:python3.10-nodejs18

# Install nginx
USER root

# Install dependencies and build app as root
ENV HOME=/root \
    PATH=$PATH

RUN mkdir $HOME/app

WORKDIR $HOME/app

# Install bun manually
RUN curl -fsSL https://bun.sh/install | bash -s -- bun-v0.5.5

# Install pynecone
RUN pip install --no-cache-dir --upgrade pynecone
RUN pip install --no-cache-dir --upgrade boto3
RUN pip install --no-cache-dir --upgrade uvicorn

# Init project
RUN pc init

# Init frontend
# Optional: could be done at runtime. But saves time if already done in container build.
#           It installs all frontend dependencies
RUN python -c "from pathlib import Path; from pynecone.utils import setup_frontend; setup_frontend(Path.cwd())"

# Copy existing project
COPY pcconfig.py pcconfig.py
COPY app app
COPY assets assets

# Re-init frontend (if new deps from project)
RUN python -c "from pathlib import Path; from pynecone.utils import setup_frontend; setup_frontend(Path.cwd())"


# Copy README and entrypoint script
COPY run.sh .

# Run script ('service nginx start' + 'pc run')
CMD ["bash", "run.sh"]
