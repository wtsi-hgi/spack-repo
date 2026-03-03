# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFloral(RPackage):
	"""Fit Log-Ratio Lasso Regression for Compositional Data

	Log-ratio Lasso regression for continuous, binary, and survival outcomes with compositional features. See Fei and others (2023) <doi:10.1101/2023.05.02.538599>.
	"""
	
	homepage = "https://vdblab.github.io/FLORAL/"
	cran = "FLORAL" 

	version("0.2.0", md5="6fa6dbdcac5c2e899e209b1ebb6d169f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-survcomp", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
