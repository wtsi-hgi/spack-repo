# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGitcreds(RPackage):
	"""Query 'git' Credentials from 'R'.

	Query, set, delete credentials from the 'git' credential store. Manage
	'GitHub' tokens and other 'git' credentials. This package is to be used by
	other packages that need to authenticate to 'GitHub' and/or other 'git'
	repositories."""

	cran = "gitcreds"

	license("MIT")

	version("0.1.2", md5="b79f9a70433189507d3eb0bdc07fae6e")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("git", type=("build", "link", "run"))
