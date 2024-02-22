# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGspcr(RPackage):
	"""Generalized Supervised Principal Component Regression

	Generalization of supervised principal component regression (SPCR; 
    Bair et al., 2006, <doi:10.1198/016214505000000628>) to support continuous, 
    binary, and discrete variables as outcomes and predictors 
    (inspired by the 'superpc' R package <https://cran.r-project.org/package=superpc>).
	"""
	
	cran = "gspcr" 

	version("0.9.4.1", md5="9583e5c3d71ad708188f589676f88b91")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mlmetrics", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-pcamixdata", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
