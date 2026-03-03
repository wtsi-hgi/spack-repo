# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGitignore(RPackage):
	"""Create Useful .gitignore Files for your Project

	Simple interface to query gitignore.io to fetch
    gitignore templates that can be included in the .gitignore file. More
    than 450 templates are currently available.
	"""
	
	homepage = "https://docs.ropensci.org/gitignore/"
	cran = "gitignore" 

	version("0.1.6", md5="14893b9e734a9bedac5bd120f6f270eb")

	depends_on("r-clipr", type=("build", "run"))
	depends_on("r-clisymbols", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-here", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-xfun", type=("build", "run"))
