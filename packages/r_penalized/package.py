# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPenalized(RPackage):
	"""L1 (Lasso and Fused Lasso) and L2 (Ridge) Penalized Estimation
in GLMs and in the Cox Model

	Fitting possibly high dimensional penalized
        regression models. The penalty structure can be any combination
        of an L1 penalty (lasso and fused lasso), an L2 penalty (ridge) and a
        positivity constraint on the regression coefficients. The
        supported regression models are linear, logistic and Poisson
        regression and the Cox Proportional Hazards model.
        Cross-validation routines allow optimization of the tuning
        parameters.
	"""
	
	cran = "penalized" 

	version("0.9-52", md5="ee0d331e346b01e6f66a0d97b0115d3d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
