# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuantilogram(RPackage):
	"""Cross-Quantilogram

	Estimation and inference methods for the cross-quantilogram.
    The cross-quantilogram is a measure of nonlinear dependence between
    two variables, based on either unconditional or conditional quantile
    functions.  The cross-quantilogram can be considered as an extension
    of the correlogram, which is a correlation function over multiple lag
    periods and mainly focuses on linear dependency.  One can use the
    cross-quantilogram to detect the presence of directional
    predictability from one time series to another.  This package provides
    a statistical inference method based on the stationary bootstrap.  See
    Linton and Whang (2007) <doi:10.1016/j.jeconom.2007.01.004> for
    univariate time series analysis and Han, Linton, Oka and Whang (2016)
    <doi:10.1016/j.jeconom.2016.03.001> for multivariate time series
    analysis.
	"""
	
	cran = "quantilogram" 

	version("2.2.1", md5="7e9771806e68b200834b22c69bd8d886")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-np", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-sparsem", type=("build", "run"))
