# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvnimpute(RPackage):
	"""Simultaneously Impute the Missing and Censored Values

	Implementing a multiple imputation algorithm for multivariate data with missing and censored values under a coarsening at random assumption (Heitjan and Rubin, 1991<doi:10.1214/aos/1176348396>). The multiple imputation algorithm is based on the data augmentation algorithm proposed by Tanner and Wong (1987)<doi:10.1080/01621459.1987.10478458>. The Gibbs sampling algorithm is adopted to to update the model parameters and draw imputations of the coarse data.
	"""
	
	homepage = "https://github.com/hli226/mvnimpute"
	cran = "mvnimpute" 

	version("1.0.1", md5="45b458f725c8dffe25935594399830cf")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-laplacesdemon", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppdist", type=("build", "run"))
