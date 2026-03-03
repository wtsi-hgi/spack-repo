# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVsp(RPackage):
	"""Vintage Sparse PCA for Semi-Parametric Factor Analysis

	Provides fast spectral estimation of latent factors in random
    dot product graphs using the vsp estimator. Under mild assumptions,
    the vsp estimator is consistent for (degree-corrected) stochastic
    blockmodels, (degree-corrected) mixed-membership stochastic
    blockmodels, and degree-corrected overlapping stochastic blockmodels.
	"""
	
	homepage = "https://github.com/RoheLab/vsp"
	cran = "vsp" 

	version("0.1.1", md5="4da176932e32de30e78fb9bea17e935d")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-invertiforms", type=("build", "run"))
	depends_on("r-lrmf3", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
