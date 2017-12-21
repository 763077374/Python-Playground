    1  pwd
    2  cd /e/mygit
    3  pwd
    4  git init
    5  subl poem.txt
    6  git add poem.txt
    7  git status
    8  git commit -m 'this poem' --author='763077374@qq.com'
    9  history
   10  git commit -m 'this poem' --author='763077374<763077374@qq.com>'
   11  git config --global user.email "763077374@qq.com"
   12  git commit -m 'this poem' --author='763077374<763077374@qq.com>'
   13  git add poem.txt 
   14  git commit -m 'next poem' --author='763077374@qq.com'
   15  gitk
   16  git commit -m 'next poem' 
   17  git config --global user.email "763077374@qq.com"
   18  git commit -m 'next poem' 
   19  git config --global user.email "763077374@qq.com"
   20  git config --global user.name "763077374"
   21  git commit -m 'next poem' 
   22  gitk
   23  exit
   24  cd /e/mygit
   25  pwd
   26  history
   27  git config -l
   28  git config --system -l
   29  git config --global -l
   30  git config alias.con 'config -l'
   31  git con
   32  git config --unset alias.con
   33  git config --global core.editor=subl.exe
   34  start.
   35  start .
   36  diff --git a/poem.txt b/poem.txt 
   37  git add *
   38  git commit * -m "a and b"
   39  diff --git a/poem.txt b/poem.txt
   40  git diff
   41  git diff a/poem.txt b/poem.txt
   42  diff --git a/poem.txt  b/poem.txt 
   43  cls
   44  clear
   45  gitk
   46  md newtest
   47  mkdir newtest
   48  cd newtest/
   49  subl poem1.txt
   50  subl poem2.txt
   51  subl poem3.txt
   52  git status
   53  cd ..
   54  cd newtest/
   55  git add poem1.txt 
   56  git commit -m '1st commit'
   57  touch .gitignore
   58  subl .gitignore 
   59  git status
   60  subl poem1.txt 
   61  subl poem2.txt
   62  subl poem3.txt 
   63  git status
   64  subl .gitignore 
   65  git show HEAD
   66  git diff HEAD HEAD^ poem1.txt
   67  git gc --auto
   68  git status
   69  dir
   70  cd ..
   71  dir
   72  ls
   73  gitk
   74  git init
   75  dir
   76  ls -l
   77  git add .
   78  git commit -m "Add poem1.txt"
   79  git branch lee-by
   80  gitk
   81  subl poem2.txt
   82  git add .
   83  git commit -m 'Add poem2.txt'
   84  subl poem3.txt
   85  git checkout lee-by
   86  git add .
   87  git commit -m 'Add poem3.txt'
   88  gitk --all
   89  git log --graph --all --decorate
   90  git checkout HEAD^
   91  git branch master 
   92  git checkout master
   93  git checkout lee-by
   94  git branch -m draft
   95  git checkout draft
   96  git checkout master
   97  git merge draft
   98  git status
   99  git branch -m commit
  100  cd ..
  101  cd App/
  102  ls
  103  git init
  104  git status
  105  git add .
  106  git commit -m 'Initial app project'
  107  ls
  108  git checkout HEAD .
  109  ls
  110  del gradle.properties 
  111  git add -A
  112  git add -A .
  113  git status
  114  git checkout HEAD .
  115  dir
  116  ls
  117  ls -l
  118  git init
  119  git status
  120  git add .
  121  sit status
  122  git status
  123  git checkout -b develop
  124  gitk
  125  git add -A
  126  git status
  127  git commit -m 'directions'
  128  git add -A .
  129  git status
  130  git commit -m 'directions'
  131  gitk
  132  git checkout develop .
  135  gitk
  136  git add .
  137  git checkout develop .
  138  ls
  139  gitk
  140  git push origin develop
  141  git push develop
  142  git config -l
  143  git branch -a
  144  git push
  145  git push develop
  146  git push --set-upstream develop develop
  147  git remote show
  148  git remote show develop
  149  git remote show egret
  150  git remote show https://github.com/763077374/egret.git
  151  get remote set-url 
  152  git remote -v
  153  git ls-remote
  154  git ls-remote
  155  get remote set-url https://github.com/763077374/method.git
  156  git remote set-url https://github.com/763077374/method.git
  157  git remote set-url  --add https://github.com/763077374/method.git
  158  git push method develop
  159  git push master develop
  160  git remote set-url  --add "https://github.com/763077374/method.git"
  161  git remote show https://github.com/763077374/egret.git
  162  git remote add origin https://github.com/763077374/method.git
  163  git push -u origin develop
  164  git clone https://github.com/professional-git/hooks.git
  165  ls
  166  git clone https://github.com/heineman/algorithms-nutshell-2ed.git
  167  cd ..
  168  mkdir pythonAlgorithms
  169  cd pythonAlgorithms/
  170  git init
  171  git status
  172  subl README.md
  174  history >> gitreadme.txt
