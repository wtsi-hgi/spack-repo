# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrecommit(RPackage):
	"""Pre-Commit Hooks

	Useful git hooks for R building on top of the multi-language
    framework 'pre-commit' for hook management. This package provides git
    hooks for common tasks like formatting files with 'styler' or spell
    checking as well as wrapper functions to access the 'pre-commit'
    executable.
	"""
	
	homepage = "https://lorenzwalthert.github.io/precommit/"
	cran = "precommit" 

	version("0.4.0", md5="b6c0a5c304a9f527e70d7468829a407a")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-here", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-r-cache", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rprojroot", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("git", type=("build", "link", "run"))
