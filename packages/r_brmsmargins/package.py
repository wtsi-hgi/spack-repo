# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrmsmargins(RPackage):
	"""Bayesian Marginal Effects for 'brms' Models

	Calculate Bayesian marginal effects, average marginal effects, and marginal coefficients (also called population averaged coefficients) for models fit using the 'brms' package including fixed effects, mixed effects, and location scale models. These are based on marginal predictions that integrate out random effects if necessary (see for example <doi:10.1186/s12874-015-0046-6> and <doi:10.1111/biom.12707>).
	"""
	
	homepage = "https://joshuawiley.com/brmsmargins/"
	cran = "brmsmargins" 

	version("0.2.0", md5="3596bd41b3a839473beeeb54ff33cb62")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-data-table@1.12:", type=("build", "run"))
	depends_on("r-extraoperators@0.1.1:", type=("build", "run"))
	depends_on("r-brms", type=("build", "run"))
	depends_on("r-bayestestr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-posterior", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
