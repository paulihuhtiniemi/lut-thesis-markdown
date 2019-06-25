#!/bin/bash
#
# author: Bastian Rieck
# ammended: Mathew Lipson
# source: http://bastian.rieck.ru/blog/posts/2017/counting_words_git/
#
# This script traverses all commits of a git repository in the current directory
# (if it exists) and counts the number of words that are changed, i.e. added or 
# deleted for all TeX files. The output contains a time-stamp (YYYY-MM-DD). Next, 
# there are some counts, viz. the number of added, deleted, and total words.
#
# Use 'branch' in order to control for which branch the commits are being enumerated.

echo "counting";

branch="master"
words=0

if [ -f log_wordcount.txt ] ; then
    rm log_wordcount.txt
fi

if [ -d .git ]; then  # list commits after initial 104
    for commit in $(git rev-list --reverse $branch)
    do
      date=$(git show -s --format=%ci $commit)
      added=$(git show -p --word-diff=porcelain $commit "source/*.md" | grep -e '^+[^+]' | wc -w)
      deleted=$(git show -p --word-diff=porcelain $commit "source/*.md" | grep -e '^-[^-]' | wc -w)
      
      words=$(($words+$added))
      words=$(($words-$deleted))
      
      echo $date +$added -$deleted Total: $words
      echo $date $words >> log_wordcount.txt
    done

    python plot_wordcount.py
else
    echo "not a git repository"
fi
