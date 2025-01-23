---
# Developing Guidelines with Branch
A comprehensive guide for team members to collaborate on this project.

---

## **Understanding the Original and Cloned Repository**

### What Is the Original Repository?
The **original repository** is the main project repository hosted on GitHub, owned by the project maintainer or organization. In this guide, the original repository is:
```
https://github.com/philtaboada/Challenge-with-EXPLOR
```
This is the **source of truth** where all approved changes will eventually be merged.

### What Is a Cloned Repository?
A **cloned repository** is a local copy of the original repository on your computer. Each team member clones the original repository to their machine to work on it locally. 

### Important Notes:
1. **You cannot directly edit the original repository** unless:
   - You are working locally on a cloned repository and pushing your changes.
   - You have been granted write access to the original repository.
2. **Changes are merged into the original repository through pull requests.**

---

## Sections in This Guide

1. [Clone the Repository](#clone-the-repository)
2. [Verify Git Repository](#verify-git-repository)
3. [Re-Cloning the Repository](#re-cloning-the-repository)
4. [Open the Repository in VS Code](#open-the-repository-in-vs-code)
5. [Create a New Branch](#create-a-new-branch)
6. [Make Changes and Commit](#make-changes-and-commit)
7. [Push the Branch to GitHub](#push-the-branch-to-github)
8. [Create a Pull Request (PR)](#create-a-pull-request-pr)
9. [Sync Your Repository with the Original Repository](#sync-your-repository-with-the-original-repository)
10. [Additional Notes](#additional-notes)

---

## Clone the Repository

1. **Open a folder** of your choice and name it `project`.
2. Clone the original repository to your local machine:
   ```bash
   git clone https://github.com/philtaboada/Challenge-with-EXPLOR
   ```

3. Navigate into the cloned directory:
   ```bash
   cd Challenge-with-EXPLOR
   ```

4. **Verify your Git setup**:
   ```bash
   git remote -v
   ```
   Expected Output:
   ```
   origin  https://github.com/philtaboada/Challenge-with-EXPLOR.git (fetch)
   origin  https://github.com/philtaboada/Challenge-with-EXPLOR.git (push)
   ```
   This confirms your cloned repository is connected to the original repository.

---

## Verify Git Repository

1. Run the following command to confirm the directory is a Git repository:
   ```bash
   git status
   ```
2. If the output shows:
   ```
   fatal: not a git repository (or any of the parent directories): .git
   ```
   This means the `.git` folder is missing. Follow the **Re-Cloning the Repository** steps below.

---

## Re-Cloning the Repository

1. Navigate to the parent directory:
   ```bash
   cd ..
   ```

2. Remove the problematic folder:
   ```bash
   rmdir /s /q Challenge_1
   ```

3. Re-clone the repository:
   ```bash
   git clone https://github.com/philtaboada/Challenge-with-EXPLOR
   ```

4. Navigate into the cloned directory:
   ```bash
   cd Challenge-with-EXPLOR
   ```

5. Confirm the repository is set up correctly:
   ```bash
   git status
   ```

---

## Open the Repository in VS Code

1. Open the cloned repository in VS Code:
   ```bash
   code .
   ```

2. Verify:
   - Check the bottom-left corner of VS Code. You should see the branch name (e.g., `main` or `feature/checking_features_built`).

---

## Create a New Branch

1. To work on a new feature or task, create and switch to a new branch:
   ```bash
   git checkout -b feature/your-branch-name
   ```

2. Push the branch to the remote repository:
   ```bash
   git push origin feature/your-branch-name
   ```

---

## Make Changes and Commit

1. **Make changes** to project files using VS Code.
2. Check the status of your changes:
   ```bash
   git status
   ```

3. Stage the changes:
   ```bash
   git add .
   ```

4. Commit your changes with a descriptive message:
   ```bash
   git commit -m "Added feature: user authentication"
   ```

---

## Push the Branch to GitHub

Push your changes to your feature branch:
```bash
git push origin feature/your-branch-name
```

---

## Create a Pull Request (PR)

1. Go to the **original repository** on GitHub.
2. Navigate to the **Pull Requests** tab and select **New Pull Request**.
3. Select:
   - **Base branch**: `main` (original repository)
   - **Compare branch**: Your feature branch
4. Add a **Title** and **Description** for the PR.
5. Submit the pull request for review.

---

## Sync Your Repository with the Original Repository

To ensure your local repository stays up-to-date with the latest changes in the original repository:

1. Add the original repository as an **upstream remote**:
   ```bash
   git remote add upstream https://github.com/philtaboada/Challenge-with-EXPLOR
   ```

2. Fetch the latest changes from the original repository:
   ```bash
   git fetch upstream
   ```

3. Merge updates from the original repository into your local `main` branch:
   ```bash
   git checkout main
   git merge upstream/main
   ```

4. Push the updated `main` branch to your fork:
   ```bash
   git push origin main
   ```

---

## Additional Notes

### Distinction Between Local, Forked, and Original Repositories
- **Local Repository**: Your Git clone on your computer.
- **Original Repository**: The main repository on GitHub (source of truth).
- **Remote Repository**: A GitHub-hosted repository you cloned or forked.

---

By adding these steps and clarifying the relationship between the original and cloned repositories, your team will better understand the process. Let me know if further adjustments are needed!
 

## Install Poetry using the developer guide-
Reference Links:
poetry: https://python-poetry.org/docs/pyproject/ 
reinstall poetry if error faced: https://stackoverflow.com/questions/70064449/how-to-force-reinstall-poetry-environment-from-scratch

**Observation:** We need to check which version of python is running in our system if it is python 3.9
then go to add/remove programs in control panel search for python delete all python versions and install the required one in this case python 3.10 was installed in the pc after removing 3.9.
**Solution:** Install python 3.10 and then install poetry using the developer guide.
**enviroment creation**: There is less flexibility in creating python environment in poetry however there is a higher flexibility if anaconda is used to create environment. eg: conda create -p myenv python==3.10 but the project in this case has to be set up with requirements.txt and setup.py for requirements and package management where the same thing can be avoided in poetry.


1. To check the python version
```bash
python --version
```
2. To install the required python version go the official python website and download the python version required make sure to check the python version by typing the above command as the virtual env created in poetry will be equal to the system python version.
3. Install Poetry by using the below command install pipx if not present in the system.
```bash 
pipx install poetry(force install again)
```
4. Check poetry is accurately installed using the command below
```bash
poetry --version
```
5. To check the base python and virtualenv version
poetry env info
6. To create virtual environment
```bash
poetry shell
```
7. To install packages
```bash
 poetry install --no-root
 ```
8. To add dependencies in poetry 
```bash
poetry add phidata
```  
9. Update the python packages
```bash
poetry update
```

- Install the required packages using poetry install
- Run the crew using poetry run main.py