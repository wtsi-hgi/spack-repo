# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStareg(RPackage):
	"""An Empirical Bayes Approach for Replicability Analysis Across
Two Studies

	A robust and powerful empirical Bayesian approach is developed for replicability analysis of two large-scale experimental studies. The method controls the false discovery rate by using the joint local false discovery rate based on the replicability null as the test statistic. An EM algorithm combined with a shape constraint nonparametric method is used to estimate unknown parameters and functions. [Li, Y. et al., (2023), <https://www.biorxiv.org/content/10.1101/2023.05.30.542607v1>].
	"""
	
	cran = "STAREG" 

	version("1.0.3", md5="4e979de918a46241fe1056ee83cad142")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
