Tutorial: How to Build a Mordern CI/CD Pipeline 
---

### Goal

- Show you the essential `building blocks` of modern software development `pipeline`
- How to `assemble` those blocks
- Understand the complete `end-to-end` pipeline

### Tutorial Steps

- Write a little Python program (not Hello World)
- Add some automated tests for the program
- Push your code to GitHub
- Setup Travis CI to continuously run your automated tests
- Setup Better Code Hub to continuously check your code quaity
- Turn the Python program into a web app
- Create a Docker image for the web app
- Push the Docker image to Docker Hub
- Deploy the Docker image to Heroku

---

- Step 1: Write a little buzz generator
    - a small piece of software that will travel through all phases of the pipeline, from your laptop to the cloud
- Step 2: Add automated tests
    - automated tests prevent you from continuous shipping broken software
- Step 3: Put the code on GitHub
    - remember to add venv in .gitignore
- Step 4: Connect Travis CI to run the tests on every commit
    - build every push and pull request to check code functionality
- Step 5: Add better code hub to the pipeline
    - check quality of the code
- Step 6: Turn the buzz generator into a simple web app    
    - Wrap the command line program with Python Flash Web app
- Step 7: Containerize your web app with docker
    - Use Docker to create a single self-contained, deployable unit of the web app
- Step 8: Deploy to Docker Hub
    - Deploy your containers to a central Docker image registry, e.g. DockerHub makes it much easier to share your container

### Todos
- [ ] Simplify the pipeline
- [ ] Setup a CI/CD template
- [ ] Fill-in the template with different components
    - Heroku -> AWS / GCP / Azure
    - Travis -> Circle CI / Jenkins / Codeship
    - Better Code Hub -> ?
    - Github -> Bitbucket
    - Python -> PHP / Java / C++ / NodeJS
    - Docker -> Vagrant + Ansible
- [ ] Fit into python template