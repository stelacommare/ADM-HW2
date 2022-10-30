#!/bin/bash

awk 'length($9) > 100 {print $5, $9}' instagram_posts.csv | head -10 > postsDesc.txt
cat postsDesc.txt  | column -t -s "       "