FROM django:latest
MAINTAINER subscriptionform

RUN useradd docker
RUN echo "ALL ALL = (ALL) NOPASSWD: ALL" >> /etc/sudoers
ENV HOME /home/docker

ADD requirements.txt $HOME/requirements.txt
ADD requirements-dev.txt $HOME/requirements-dev.txt
RUN pip install -r $HOME/requirements-dev.txt
RUN rm $HOME/requirements.txt $HOME/requirements-dev.txt

# Switch to docker user.
RUN chown -R docker:docker $HOME/
USER docker

ENV DEBUG 1
ENV DATABASE_URL mysql://subscriptionform:subscriptionform@db/subscriptionform

WORKDIR /home/docker/subscriptionform
