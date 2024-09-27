# Basic Git understanding
 
Go to your folder of choice:
 
```bash
cd /OneDrive/Documents/Github/tech264-test-git
```
 
Initialise the repository:
 
```bash
git init
```
 
Create the README.md file:
 
```bash
touch README.md
```
 
Modify the file
 
Add file to stage:
 
```bash
git add README.md
```
 
Commit changes:
 
```bash
git commit -m "My first commit"
```
 
Modify the file again
 
Add file to stage:
 
```bash
git add README.md
```
 
Commit changes:
 
```bash
git commit -m "My second commit"
```
 
Check the changes
 
```bash
git checkout
```
```bash
git log
```
# Version Control System (VCS)

## What is a Version Control System (VCS)?
A **Version Control System (VCS)** is a tool that helps track and manage changes to files (usually code) over time by maintaining a history of file versions. It allows multiple users to collaborate efficiently on a shared codebase.

---

## When to Use a VCS?
- For **software development** projects with frequent updates.
- In **collaborative environments** where multiple developers need to work on the same codebase.
- To maintain a **history of changes** and enable easy reversion to previous versions.
- For **experimenting** with new features without disrupting the main project.

---

## Benefits of Using a VCS
- **History tracking**: Keeps a record of every change, allowing for easy comparison and restoration of previous versions.
- **Collaboration**: Multiple developers can work on the same project simultaneously.
- **Branching and merging**: Allows feature development in parallel, enabling changes to be merged back into the main codebase.
- **Backup**: Ensures a backup of the codebase is stored centrally or distributed among developers.

---

## Types of Version Control
1. **Local Version Control**: Versions are managed on a single machine (e.g., RCS).
2. **Centralized Version Control (CVCS)**: All versions are stored on a central server (e.g., SVN, CVS).
3. **Distributed Version Control (DVCS)**: Every developer has a full copy of the repository, allowing offline work (e.g., Git, Mercurial).

---

## What is Manual Version Control?
- Involves manually saving multiple versions of files (e.g., `file_v1`, `file_v2`) without using a VCS tool.
- Error-prone and difficult to manage for large projects or multiple contributors.

---

## How Did Early Version Control Systems Work?
- Early VCSs like **RCS (Revision Control System)** stored revisions in a single file.
- They allowed tracking individual changes and rolling back to earlier versions.
- Operated on local machines, making collaboration difficult.

---

## Centralized VCS vs Distributed VCS

### Centralized VCS (CVCS)
- A **single server** holds the entire codebase and version history.
- Users check out copies from the server, and all changes must be committed to the server.
- Examples: **SVN**, **CVS**.
  
### Distributed VCS (DVCS)
- Each developer has a **full copy** of the repository, including history.
- Users can work **offline**, committing changes locally and synchronizing with others via push/pull operations.
- Examples: **Git**, **Mercurial**.

![Git vs Centralized VCS](https://www.atlassian.com/git/images/tutorials/cdvcs_vs_dvcs_2x.png)  
*Source: Atlassian Git Tutorial*

---

## Local Version Control with Git

### What is Stored in Each Version of a File That Changes?
- Git stores **snapshots** of the file at each commit, rather than keeping track of differences line by line.
- Only files that have **changed** since the last commit are stored.

### Does Git Need to Be Used as a Distributed VCS?
- No, Git can be used as a **local** version control system without connecting to any remote repositories.
- However, Git's power lies in its **distributed** nature, which enables collaboration across teams.

### What Does Git Store in a 'Commit'?
- A commit in Git contains:
  - A **snapshot** of all files at the time of the commit.
  - A **commit message** describing the change.
  - Metadata such as **author**, **timestamp**, and **parent commit** reference(s).

---

## The Three States in Git
1. **Modified**: Files have been changed but not yet staged for commit.
2. **Staged**: Changes are marked to be included in the next commit.
3. **Committed**: The changes are safely stored in the local repository.

---

## Where Does Git Store Its Information?
- Git stores its information in a hidden directory called `.git` located at the root of your project directory.
- This folder contains the **repository’s metadata**, **commit history**, **branch references**, and **staging area**.

---

## Common Workflow of Git Commands
1. `git init` – Initialize a new Git repository.
2. `git add` – Stage files for commit.
3. `git commit` – Commit changes to the local repository.
4. `git push` – Push changes to a remote repository.
5. `git pull` – Pull updates from a remote repository.
6. `git status` – Check the current state of the working directory and staging area.
7. `git branch` – Create, list, or delete branches.
8. `git merge` – Merge changes from one branch into another.
