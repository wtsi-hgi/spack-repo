# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGitear(RPackage):
	"""Client to the 'gitea' API

	'Gitea' is a community managed, lightweight code hosting solution 
  were projects and their respective git repositories can be managed 
  <https://gitea.io>. This package gives an interface to the 'Gitea' API to 
  access and manage repositories, issues and organizations directly in R. 
	"""
	
	homepage = "https://ixpantia.github.io/gitear/"
	cran = "gitear" 

	version("1.0.0", md5="0b31db8dd56b8988900d008bfa9480a6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-mockery", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
