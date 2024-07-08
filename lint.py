#!/usr/bin/env python

import glob
import re
import yaml

def getPostMetadata(post):
    handle = open(post, "r")
    lines = handle.read()
    handle.close()

    content = re.search(r"---(.*)---", lines, re.DOTALL).group(1)
    content = content.strip()

    postMetadata = yaml.load(content, Loader=yaml.FullLoader)
    postMetadata["path"] = post

    return postMetadata

def getAllPostMetadata():
    posts = glob.glob("content/posts/*/*.md", recursive=True)

    postMetadata = []

    for post in posts:
        postMetadata.append(getPostMetadata(post))

    return postMetadata

def lint():
    postMetadata = getAllPostMetadata()

    for post in postMetadata:
        if "title" not in post:
            print("Title not found in post: " + post["path"])

        if "date" not in post:
            print("Date not found in post: " + post["path"])

        if "tags" not in post:
            print("Tags not found in post: " + post["path"])

        tags = post["tags"]

        # Lint message if tags does not contain 1 continent
        if tags.count("Africa") + tags.count("Asia") + tags.count("Europe") + tags.count("America") + tags.count("Oceania") != 1:
            print("Post does not contain exactly 1 continent: " + post["path"])


lint()
