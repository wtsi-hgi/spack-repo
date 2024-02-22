# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROsfr(RPackage):
	"""Interface to the 'Open Science Framework' ('OSF')

	An interface for interacting with 'OSF' (<https://osf.io>). 'osfr'
    enables you to access open research materials and data, or create and
    manage your own private or public projects.
	"""
	
	homepage = "https://docs.ropensci.org/osfr/"
	cran = "osfr" 

	version("0.2.9", md5="81240e1be00c50cd91131b7ea4aa296c")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-crul@0.7.4:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-fs@1.3:", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
