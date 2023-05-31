# Prefect Poetry Copier Setup

## Quickstart
- Create a new repository and clone that empty repository to your local machine
- Ensure that [copier](https://copier.readthedocs.io/en/stable/) is installed
- Ensure that [just](https://just.systems/man/en/) is installed
- From your local repository run `copier https://github.com/ngriffiths13/prefect-poetry-setup.git .`
- Answer the questions that copier asks you and you should be good to go!
- Find all the places in the repo marked with `#TODO` and fill in the appropriate values
- Check the [Post-Setup](#post-setup) section for some additional steps you may want to take

## Description
This is a project structure setup according to my own biases and preferences but is hopefully helpful
to others as well. It currently only supports the most basic of deployment setups, but depending on the
interest, I may add others. See below to see what is and is not currently supported. I am hopeful that even
if your preferred tools are not yet supported, the structure of the project will be helpful to you.

The project sets up Prefect for deployments using the projects feature. The whole repository is based around
using poetry as a package manager and includes all the files you would need to get started with
deploying prefect.

## Features
### Storage
- [x] Github
- [ ] Gitlab
- [ ] Bitbucket
- [ ] GCS
- [ ] S3

### Deployment
- [x] Local
- [x] Docker
- [ ] Kubernetes
- [ ] ECS
- [x] Google Cloud Run

### CI/CD
- [x] Github Actions
- [ ] Gitlab CI
- [ ] Bitbucket Pipelines
- [ ] Cloudbuild

### Docker Registry
- [x] Dockerhub
- [ ] Github Container Registry
- [ ] AWS ECR
- [ ] Google Container Registry
- [x] Google Artifact Registry

## Usage
The repository is set up with the following tools and files:
- [Poetry](https://python-poetry.org/) for package management
  - A pyproject.toml will be generated for you with the poetry configuration, the appropriate prefect libraries, a few dev dependencies, and a few helpful configurations for other tools such as pytest, ruff, and coverage.
- [Just](https://just.systems/man/en/) for task running
  - A justfile will be generated for you with a few helpful commands for running tests, linting, and building the docker image locally.
  - You can run `just --list` to see all the available commands.
- [Prefect](https://www.prefect.io/) for workflow management
  - A deployment.yaml file will be generated for you containing and example deployment, along with the a resuable work pool to attach to your deployments. A command to create that work pool is added to your `justfile`.
  - A prefect.yaml file will be generated containing the configured storage and builds for your project.
- CI/CD files will be created to help with checking tests and linting, along with deploying projects.
- [Docker](https://docs.docker.com/get-started/) files will be created to help with building and deploying docker images. A multistage build Dockerfile is included to help cut image size down.
- [Noxfile](https://nox.thea.codes/en/stable/) will be created to help with running tests locally in a clean environment.

## Post-Setup <a name="post-setup"></a>
### Secrets and Environment Variables
Depending on your setup you will need to add some secrets and environment variables to your repository.
They are organized based on the tools you choose to use.

**Github Actions**
- *Github Secrets*:
  - `PREFECT_API_KEY`
  - `PREFECT_WORKSPACE`
- *Prefect Secrets Block*:
  - `github-access-token`

**Dockerhub**
- *Github Secrets*:
  - `DOCKERHUB_USERNAME`
  - `DOCKERHUB_TOKEN`