# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCcpsyc(RPackage):
	"""Methods for Cross-Cultural Psychology

	With the development of new cross-cultural methods this package is intended to combine multiple functions automating and simplifying functions providing a unified analysis approach for commonly employed methods. 
	"""
	
	cran = "ccpsyc" 

	version("0.2.6", md5="503b71bfc7d3284d0fb6f62394f9e519")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-ufs", type=("build", "run"))
	depends_on("r-xlsx", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcppalgos", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
