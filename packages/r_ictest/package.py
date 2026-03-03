# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIctest(RPackage):
	"""Estimating and Testing the Number of Interesting Components in
Linear Dimension Reduction

	For different linear dimension reduction methods like principal components analysis (PCA), independent components analysis (ICA) and supervised linear dimension reduction tests and estimates for the number of interesting components (ICs) are provided.
	"""
	
	cran = "ICtest" 

	version("0.3-5", md5="6410b1c2c054e911bcfb89f4d58ed280")

	depends_on("r-jade", type=("build", "run"))
	depends_on("r-ics@1.3.0:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-icsnp", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-rcpproll", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
