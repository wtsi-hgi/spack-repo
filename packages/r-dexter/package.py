# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDexter(RPackage):
	"""Data Management and Analysis of Tests

	A system for the management, assessment, and psychometric analysis of data from educational and psychological tests. 
	"""
	
	homepage = "https://dexter-psychometrics.github.io/dexter/"
	cran = "dexter" 

	version("1.4.0", md5="89b728a5cd0bfb9563c9101b6f54f950")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rsqlite@2.2.7:", type=("build", "run"))
	depends_on("r-dbi@1:", type=("build", "run"))
	depends_on("r-mass@7.3:", type=("build", "run"))
	depends_on("r-tidyr@1.2:", type=("build", "run"))
	depends_on("r-rlang@0.4.1:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.12.6.6:", type=("build", "run"))
	depends_on("r-dqrng", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-sitmo", type=("build", "run"))
