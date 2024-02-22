# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutonewsmd(RPackage):
	"""Auto-Generate Changelog using Conventional Commits

	Automatically generate a changelog file (NEWS.md /
    CHANGELOG.md) from the git history using conventional commit messages
    (<https://www.conventionalcommits.org/en/v1.0.0/>).
	"""
	
	homepage = "https://github.com/kapsner/autonewsmd"
	cran = "autonewsmd" 

	version("0.0.6", md5="c42e0587b08190a1d27d3c759b07cd7b")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-git2r", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
