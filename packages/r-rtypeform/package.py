# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtypeform(RPackage):
	"""Interface to 'typeform' Results

	An R interface to the 'typeform'
    <https://typeform.com> application program interface.  Also provides
    functions for downloading your results.
	"""
	
	homepage = "https://github.com/csgillespie/rtypeform"
	cran = "rtypeform" 

	version("2.1.0", md5="830eb6d2c018e325730bec1a60ab7f43")

	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
