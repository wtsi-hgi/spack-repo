# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBmggum(RPackage):
	"""Bayesian Multidimensional Generalized Graded Unfolding Model

	Full Bayesian estimation of Multidimensional Generalized Graded Unfolding Model (MGGUM) using 'rstan' (See Stan Development Team (2020) <https://mc-stan.org/>).
    Functions are provided for estimation, result extraction, model fit statistics, and plottings.
	"""
	
	homepage = "https://github.com/Naidantu/bmggum"
	cran = "bmggum" 

	version("0.1.0", md5="285740666f913e9655a5975452e7e00d")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-rstantools@2.1.1:", type=("build", "run"))
	depends_on("r-edstan", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggum", type=("build", "run"))
	depends_on("r-loo", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
