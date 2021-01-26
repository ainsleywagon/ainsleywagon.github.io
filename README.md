
# Ainsley Wagoner Portfolio

Using monfresh's script to keep ruby env and jekyll gems up to date:
https://github.com/monfresh/laptop

Script here:
```bash <(curl -s https://raw.githubusercontent.com/monfresh/laptop/master/laptop)```
Run this to update this

```Jekyll serve``` to spin up the local site

Keeping project in sync with gh-pages:
```git add .
git status // to see what changes are going to be commited
git commit -m 'Some descriptive commit message'
git push origin master

git checkout gh-pages // go to the gh-pages branch
git merge master // bring gh-pages up to date with master
git push origin gh-pages // commit the changes
git checkout master // return to the master branch
```
