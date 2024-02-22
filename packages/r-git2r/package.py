# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGit2r(RPackage):
	"""Provides Access to Git Repositories.

	Interface to the 'libgit2' library, which is a pure C implementation of the
	'Git' core methods. Provides access to 'Git' repositories to extract data
	and running some basic 'Git' commands."""

	cran = "git2r"

	version("0.33.0", md5="5bb26ea3f304fd762ecc3a770fc94a8a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("libgit2", type=("build", "link", "run"))
