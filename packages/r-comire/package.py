# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComire(RPackage):
	"""Convex Mixture Regression

	Posterior inference under the convex mixture regression (CoMiRe) models introduced by Canale, Durante, and Dunson (2018) <doi:10.1111/biom.12917>.
	"""
	
	cran = "CoMiRe" 

	version("0.8", md5="08d96b03921d8458a3a530d5e3f6ba75")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp@1.0.5:", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-splines2@0.3.1:", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
