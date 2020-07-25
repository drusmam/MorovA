Last login: Sat Jul 25 09:03:18 on ttys001
(base) andreimorau@MacBook-Pro-Andrei ~ % git --version
git version 2.24.3 (Apple Git-128)
(base) andreimorau@MacBook-Pro-Andrei ~ % git config --list --show-origin
file:/Library/Developer/CommandLineTools/usr/share/git-core/gitconfig   credential.helper=osxkeychain
file:/Users/andreimorau/.gitconfig      user.email=drusmam@gmail.com
file:/Users/andreimorau/.gitconfig      user.name=Mam Mam
file:/Users/andreimorau/.gitconfig      core.excludesfile=/Users/andreimorau/.gitignore_global
file:/Users/andreimorau/.gitconfig      difftool.sourcetree.cmd=opendiff "$LOCAL" "$REMOTE"
file:/Users/andreimorau/.gitconfig      difftool.sourcetree.path=
file:/Users/andreimorau/.gitconfig      mergetool.sourcetree.cmd=/Applications/Sourcetree.app/Contents/Resources/opendiff-w.sh "$LOCAL" "$REMOTE" -ancestor "$BASE" -merge "$MERGED"
file:/Users/andreimorau/.gitconfig      mergetool.sourcetree.trustexitcode=true
(base) andreimorau@MacBook-Pro-Andrei ~ % git config --list
credential.helper=osxkeychain
user.email=drusmam@gmail.com
user.name=Mam Mam
core.excludesfile=/Users/andreimorau/.gitignore_global
difftool.sourcetree.cmd=opendiff "$LOCAL" "$REMOTE"
difftool.sourcetree.path=
mergetool.sourcetree.cmd=/Applications/Sourcetree.app/Contents/Resources/opendiff-w.sh "$LOCAL" "$REMOTE" -ancestor "$BASE" -merge "$MERGED"
mergetool.sourcetree.trustexitcode=true
(base) andreimorau@MacBook-Pro-Andrei ~ % git clone https://github.com/drusmam/python_tasks   
Cloning into 'python_tasks'...
warning: You appear to have cloned an empty repository.
(base) andreimorau@MacBook-Pro-Andrei ~ % git clone https://github.com/drusmam/python_tasks-1 PycharmProjects
fatal: destination path 'PycharmProjects' already exists and is not an empty directory.
(base) andreimorau@MacBook-Pro-Andrei ~ % git clone https://github.com/drusmam/python_tasks-1 PycharmProjects/1
Cloning into 'PycharmProjects/1'...
remote: Enumerating objects: 39, done.
remote: Counting objects: 100% (39/39), done.
remote: Compressing objects: 100% (26/26), done.
remote: Total 39 (delta 10), reused 30 (delta 9), pack-reused 0
Unpacking objects: 100% (39/39), done.
(base) andreimorau@MacBook-Pro-Andrei ~ % git status
fatal: not a git repository (or any of the parent directories): .git
(base) andreimorau@MacBook-Pro-Andrei ~ % ls
12345.txt				Movies
Applications				Music
Applications (Parallels)		Parallels
Creative Cloud Files			Pictures
Desktop					Public
Documents				PycharmProjects
Downloads				VirtualBox VMs
Dropbox					Windows_VB
Google Drive File Stream		get-pip.py
Google Диск				iCloud Drive (архив)
Google Диск (a.morov@imlab.by)		iCloud Drive (архив) - 1
Google Диск (drusmam@gmail.com)		iCloud Drive (архив) - 2
Guess_code.ipynb			opt
JupyterRoot				Документы
Library
(base) andreimorau@MacBook-Pro-Andrei ~ % cd PycharmProjects
(base) andreimorau@MacBook-Pro-Andrei PycharmProjects % ls
home_work	python_tasks-1	untitled
(base) andreimorau@MacBook-Pro-Andrei PycharmProjects % cd home_work
(base) andreimorau@MacBook-Pro-Andrei home_work % git status
On branch master
Your branch is up to date with 'origin/master'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.idea/

nothing added to commit but untracked files present (use "git add" to track)
(base) andreimorau@MacBook-Pro-Andrei home_work % git clone https://github.com/drusmam/MorovA PycharmProjects/1
Cloning into 'PycharmProjects/1'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), done.
(base) andreimorau@MacBook-Pro-Andrei home_work % cd PycharmProjects
cd: no such file or directory: PycharmProjects
(base) andreimorau@MacBook-Pro-Andrei home_work % cd /PycharmProjects
cd: no such file or directory: /PycharmProjects
(base) andreimorau@MacBook-Pro-Andrei home_work % cd ..
(base) andreimorau@MacBook-Pro-Andrei PycharmProjects % 
(base) andreimorau@MacBook-Pro-Andrei PycharmProjects % git clone https://github.com/drusmam/MorovA
Cloning into 'MorovA'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), done.
(base) andreimorau@MacBook-Pro-Andrei PycharmProjects % cd MorovA
(base) andreimorau@MacBook-Pro-Andrei MorovA % git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.idea/

nothing added to commit but untracked files present (use "git add" to track)
(base) andreimorau@MacBook-Pro-Andrei MorovA % gid add
zsh: command not found: gid
(base) andreimorau@MacBook-Pro-Andrei MorovA % gid add HW_1_1.py
zsh: command not found: gid
(base) andreimorau@MacBook-Pro-Andrei MorovA % git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.idea/

nothing added to commit but untracked files present (use "git add" to track)
(base) andreimorau@MacBook-Pro-Andrei MorovA % git status 
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   HW_1_1.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.idea/

no changes added to commit (use "git add" and/or "git commit -a")
(base) andreimorau@MacBook-Pro-Andrei MorovA % git add HW_1_1.py
(base) andreimorau@MacBook-Pro-Andrei MorovA % git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   HW_1_1.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.idea/

(base) andreimorau@MacBook-Pro-Andrei MorovA % vim HW_1_1.py

# бум тестить
# изменняем файл
#еще одно изменение     
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
-- INSERT --
