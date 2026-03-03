# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGitdown(RPackage):
	"""Turn Your Git Commit Messages into a HTML Book

	Read all commit messages of your local git repository and
    sort them according to tags or specific text pattern into chapters of
    a HTML book using 'bookdown'. The git history book presentation helps
    organisms required to testify for every changes in their source code,
    in relation to features requests.
	"""
	
	homepage = "https://thinkr-open.github.io/gitdown/"
	cran = "gitdown" 

	version("0.1.6", md5="620afc3ab7d4fb82fd46e3ebff5f613d")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-attempt", type=("build", "run"))
	depends_on("r-bookdown", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-git2r@0.26:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
