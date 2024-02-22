# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMonashtipr(RPackage):
	"""An R API Wrapper for the Monash University Probabilistic Footy
Tipping Competition

	An API wrapper for the 'Monash University Probabilistic Footy 
    Tipping Competition' <https://probabilistic-footy.monash.edu/~footy/index.shtml>. 
    Allows users to submit tips directly to the competition from R.
	"""
	
	homepage = "https://jimmyday12.github.io/monash_tipr/"
	cran = "monashtipr" 

	version("0.1.0", md5="8c8a2ea1ec34e0fd482281fadc44051d")

	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
