# See https://hub.docker.com/r/nikolaik/python-nodejs
#     https://github.com/nikolaik/docker-python-nodejs
# Default user is 'pn' with uid 1000, gid 1000
FROM nikolaik/python-nodejs:python3.10-nodejs18

# Install nginx and give permissions to 'pn'
# See https://www.rockyourcode.com/run-docker-nginx-as-non-root-user/
USER root

RUN apt-get -y update && apt-get -y install nginx

RUN mkdir -p /var/cache/nginx \
             /var/log/nginx \
             /var/lib/nginx
RUN touch /var/run/nginx.pid

RUN chown -R pn:pn /var/cache/nginx \
                       /var/log/nginx \
                       /var/lib/nginx \
                       /var/run/nginx.pid

# Install dependencies and build app as non-root
USER pn
ENV HOME=/home/pn \
    PATH=/home/pn/.local/bin:$PATH

RUN mkdir $HOME/app

WORKDIR $HOME/app

# Install bun manually
RUN curl -fsSL https://bun.sh/install | bash

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
COPY --chown=pn pcconfig.py pcconfig.py
COPY --chown=pn app app
COPY --chown=pn assets assets

# Re-init frontend (if new deps from project)
ENV PORT=$PORT
RUN python -c "from pathlib import Path; from pynecone.utils import setup_frontend; setup_frontend(Path.cwd())"

# Copy nginx configuration
COPY --chown=pn nginx.conf /etc/nginx/sites-available/default

# Copy README and entrypoint script
COPY --chown=pn run.sh .

# Run script ('service nginx start' + 'pc run')
CMD ["bash", "run.sh"]
