#### using git
- environment:ubuntu18.04/windows10-Git bash

1.单人开发项目流程操作
```
# clone项目,http方式或者ssh链接
git clone http/ssh(test)
# 进入项目
cd test
# git 初始化
git init
# 新建开发者分支，习惯master作为发布分支,develop作为开发分支供测试开发
git checkout -b develop
# 查看当前分支，确认是否在develop
git branch
# 新建readme
touch README.md
# 添加readme
git add README.md
# 描述此节点的描述信息
git commit -m "first git test"
# 推送到develop分支
git push origin develop
# ...
# 满足一定功能并测试后，切换回master
git checkout master
# 合并develop到master
git merge develop
# 给当前发布版本打标签
git tag -a v1.0 -m 'test system v1.0'
```
