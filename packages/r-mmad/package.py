# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmad(RPackage):
	"""MM Algorithm Based on the Assembly-Decomposition Technology

	The Minorize-Maximization(MM) algorithm based on Assembly-Decomposition(AD) technology can be used for model estimation of parametric models, semi-parametric models and non-parametric models. We selected parametric models including left truncated normal distribution, type I multivariate zero-inflated generalized poisson distribution and multivariate compound zero-inflated generalized poisson distribution; semiparametric models include Cox model and gamma frailty model; nonparametric model is estimated for type II interval-censored data. These general methods are proposed based on the following papers,
    Tian, Huang and Xu (2019) <doi:10.5705/SS.202016.0488>,
    Huang, Xu and Tian (2019) <doi:10.5705/ss.202016.0516>,
    Zhang and Huang (2022) <doi:10.1117/12.2642737>.
	"""
	
	cran = "MMAD" 

	version("1.0.0", md5="99d762dd332436856b431f54561fd7db")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
