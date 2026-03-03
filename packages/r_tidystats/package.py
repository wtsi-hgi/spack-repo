# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidystats(RPackage):
	"""Save Output of Statistical Tests

	Save the output of statistical tests in an organized file that can 
  be shared with others or used to report statistics in scientific papers.
	"""
	
	homepage = "https://willemsleegers.github.io/tidystats/"
	cran = "tidystats" 

	version("0.6.0", md5="7061909abd990b46ef766b6292456a60")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
