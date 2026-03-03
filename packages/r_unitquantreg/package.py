# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnitquantreg(RPackage):
	"""Parametric Quantile Regression Models for Bounded Data

	A collection of parametric quantile regression models for bounded data. At present, the package provides 13 parametric quantile regression models. It can specify regression structure for any quantile and shape parameters. It also provides several S3 methods to extract information from fitted model, such as residual analysis, prediction, plotting, and model comparison. For more computation efficient the [dpqr]'s, likelihood, score and hessian functions are written in C++. For further details see Mazucheli et. al (2022) <doi:10.1016/j.cmpb.2022.106816>.
	"""
	
	homepage = "https://andrmenezes.github.io/unitquantreg/"
	cran = "unitquantreg" 

	version("0.0.6", md5="b788fb298e90c98afca4f35accb843b5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
