# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFmf(RPackage):
	"""Fast Class Noise Detector with Multi-Factor-Based Learning

	A fast class noise detector which provides noise score for each observations. The package takes advantage of 'RcppArmadillo' to speed up the calculation of distances between observations.
	"""
	
	cran = "fmf" 

	version("1.1.1", md5="ba769fa9ad015bac8c2b9fec016dca45")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-solitude", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-c50", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-factoextra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("armadillo", type=("build", "link", "run"))
	depends_on("lapack", type=("build", "link", "run"))
	depends_on("blas", type=("build", "link", "run"))
	depends_on("arpack-ng", type=("build", "link", "run"))
	depends_on("gcc", type=("build", "link", "run"))
