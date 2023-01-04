This is a README, read it well, read it deep, internalize it.

### Git Tagging

`git tag -a <tagname> -m "<commit_message>` -> makes an annotated tag

`git push origin <tagname>` -> pushes a specific tag to the remote server

`git push origin --tags` -> will push all tags, lightweight and annotated

`git push origin --follow-tags` -> pushes only annotated tags to the remote

`git tag -d <tagname>` -> deletes a tag locally

`git push origin :refs/tags/<tagname>` -> pushes a null refences to that remote reference (null before colon)

`git push origin --delete <tagname>` -> Same thing, but more intuitive
