# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDesla(RPackage):
	"""Desparsified Lasso Inference for Time Series

	Calculates the desparsified lasso as originally introduced in van de Geer et al. (2014) <doi:10.1214/14-AOS1221>, and provides inference suitable for high-dimensional time series, based on the long run covariance estimator in Adamek et al. (2020) <arXiv:2007.10952>. Also estimates high-dimensional local projections by the desparsified lasso, as described in Adamek et al. (2022) <arXiv:2209.03218>.
	"""
	
	homepage = "https://github.com/RobertAdamek/desla"
	cran = "desla" 

	version("0.3.0", md5="409c3c83e8922b02b277e0e43cf05fc0")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-parallelly", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-sitmo", type=("build", "run"))
