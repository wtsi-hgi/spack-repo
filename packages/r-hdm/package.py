# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdm(RPackage):
	"""High-Dimensional Metrics

	Implementation of selected high-dimensional statistical and
    econometric methods for estimation and inference. Efficient estimators and
    uniformly valid confidence intervals for various low-dimensional causal/
    structural parameters are provided which appear in high-dimensional
    approximately sparse models. Including functions for fitting heteroscedastic
    robust Lasso regressions with non-Gaussian errors and for instrumental variable
    (IV) and treatment effect estimation in a high-dimensional setting. Moreover,
    the methods enable valid post-selection inference and rely on a theoretically
    grounded, data-driven choice of the penalty.
    Chernozhukov, Hansen, Spindler (2016) <arXiv:1603.01700>.
	"""
	
	cran = "hdm" 

	version("0.3.2", md5="c81019083302632e383080df5f343614")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
