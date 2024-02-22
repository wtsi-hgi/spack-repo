# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGert(RPackage):
	"""Simple Git Client for R.

	Simple git client for R based on 'libgit2' with support for SSH and  HTTPS
	remotes. All functions in 'gert' use basic R data types (such as vectors
	and data-frames) for their arguments and return values. User credentials
	are shared with command line 'git' through the git-credential store and ssh
	keys stored on disk or ssh-agent."""

	cran = "gert"

	version("2.0.1", md5="2efae501b706f98b74f97f9a8a5b7d38")

	depends_on("r-askpass", type=("build", "run"))
	depends_on("r-credentials@1.2.1:", type=("build", "run"))
	depends_on("r-openssl@2.0.3:", type=("build", "run"))
	depends_on("r-rstudioapi@0.11:", type=("build", "run"))
	depends_on("r-sys", type=("build", "run"))
	depends_on("r-zip@2.1:", type=("build", "run"))
	depends_on("libgit2", type=("build", "link", "run"))
