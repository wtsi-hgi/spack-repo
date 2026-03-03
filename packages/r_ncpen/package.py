# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNcpen(RPackage):
	"""Unified Algorithm for Non-convex Penalized Estimation for
Generalized Linear Models

	An efficient unified nonconvex penalized estimation algorithm for
    Gaussian (linear), binomial Logit (logistic), Poisson, multinomial Logit,
    and Cox proportional hazard regression models.
    The unified algorithm is implemented based on the convex concave procedure and
    the algorithm can be applied to most of the existing nonconvex penalties.
    The algorithm also supports convex penalty:
    least absolute shrinkage and selection operator (LASSO).
    Supported nonconvex penalties include
    smoothly clipped absolute deviation (SCAD),
    minimax concave penalty (MCP), truncated LASSO penalty (TLP),
    clipped LASSO (CLASSO), sparse ridge (SRIDGE),
    modified bridge (MBRIDGE) and modified log (MLOG).
    For high-dimensional data (data set with many variables),
    the algorithm selects relevant variables producing a parsimonious regression model.
    Kim, D., Lee, S. and Kwon, S. (2018) <arXiv:1811.05061>,
    Lee, S., Kwon, S. and Kim, Y. (2016) <doi:10.1016/j.csda.2015.08.019>,
    Kwon, S., Lee, S. and Kim, Y. (2015) <doi:10.1016/j.csda.2015.07.001>.
    (This research is funded by Julian Virtue Professorship from Center for Applied Research at Pepperdine
    Graziadio Business School and the National Research Foundation of Korea.)
	"""
	
	homepage = "https://github.com/zeemkr/ncpen"
	cran = "ncpen" 

	version("1.0.0", md5="6b658d1c70ef295102781f1e66a418a6")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
