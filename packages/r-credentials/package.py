# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCredentials(RPackage):
	"""Tools for Managing SSH and Git Credentials.

	Setup and retrieve HTTPS and SSH credentials for use with 'git' and other
	services. For HTTPS remotes the package interfaces the 'git-credential'
	utility which 'git' uses to store HTTP usernames and passwords. For SSH
	remotes we provide convenient functions to find or generate appropriate SSH
	keys. The package both helps the user to setup a local git installation,
	and also provides a back-end for git/ssh client libraries to authenticate
	with existing user credentials."""

	cran = "credentials"

	license("MIT")

	version("2.0.1", md5="7d4f697f7af872bfa8ccaf1326d5d650")

	depends_on("r-openssl@1.3:", type=("build", "run"))
	depends_on("r-sys@2.1:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-askpass", type=("build", "run"))
	depends_on("git", type=("build", "link", "run"))
