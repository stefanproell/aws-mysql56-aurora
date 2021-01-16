# Working with AWS Aurora
Snippets for working with AWS MySQL Aurora

## Connect to AWS Aurora MySQL 5.6 with TLSv1

Ubuntu and many other Linux distributions dropped support for TLSv1 for security reasons.
Since AWS Aurora MySQL 5.6 only supports TLSv1 for encrypted connections a work around is needed.
See details at [my blog](https://www.stefanproell.at/posts/2020-08-18-ubuntu20-04-01-mysql5.6/) and in this repository in the folder `aws-mysql56-ubuntu-python`.
