# Basic Flask API  in a CI/CD pipeline

This repository contains : 
- Github Action's workflow file
- Dockerfile 
- requirements.txt
- main.py

For each git push/pull request, Github Action's workflow is triggered. (see .github/workflows/ci.yml for more details)

Here are the differents steps : 
- Repository checkout
- Set up Python version
- Login into Docker using 'docker/login-action'
- Build and Push using 'docker/build-push-action'
