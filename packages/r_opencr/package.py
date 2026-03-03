# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpencr(RPackage):
	"""Open Population Capture-Recapture

	Non-spatial and spatial open-population capture-recapture analysis.
	"""
	
	homepage = "https://www.otago.ac.nz/density/"
	cran = "openCR" 

	version("2.2.6", md5="9f0a2132e2a21c044fc1325bd5f67b5c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-secr@4.6.1:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
