###### using git
- environment:ubuntu18.04/windows10-Git bash

1.单人开发项目流程操作
```
git clone http/ssh(test)
cd test
git init
git checkout -b develop
git branch
touch README.md
git add README.md
git commit -m "first git test"
git push origin develop
git checkout master
git merge develop
```
