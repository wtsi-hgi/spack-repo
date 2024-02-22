# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVarshrink(RPackage):
	"""Shrinkage Estimation Methods for Vector Autoregressive Models

	
    Vector autoregressive (VAR) model is a fundamental and effective approach
    for multivariate time series analysis. Shrinkage estimation methods can be
    applied to high-dimensional VAR models with dimensionality greater than
    the number of observations, contrary to the standard ordinary least squares
    method. This package is an integrative package delivering nonparametric,
    parametric, and semiparametric methods in a unified and consistent manner,
    such as the multivariate ridge regression in Golub, Heath, and Wahba (1979)
    <doi:10.2307/1268518>, a James-Stein type nonparametric shrinkage method in
    Opgen-Rhein and Strimmer (2007) <doi:10.1186/1471-2105-8-S2-S3>, and
    Bayesian estimation methods using noninformative and informative priors
    in Lee, Choi, and S.-H. Kim (2016) <doi:10.1016/j.csda.2016.03.007> and
    Ni and Sun (2005) <doi:10.1198/073500104000000622>.
	"""
	
	homepage = "https://github.com/namgillee/VARshrink/"
	cran = "VARshrink" 

	version("0.3.1", md5="d9b3d8b18f375015ada80c4af8224444")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-vars@1.5.3:", type=("build", "run"))
	depends_on("r-ars@0.6:", type=("build", "run"))
	depends_on("r-corpcor@1.6.9:", type=("build", "run"))
	depends_on("r-strucchange", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
