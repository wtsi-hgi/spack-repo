# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSandwich(RPackage):
	"""Robust Covariance Matrix Estimators.

	Object-oriented software for model-robust covariance matrix estimators.
	Starting out from the basic  robust Eicker-Huber-White sandwich covariance
	methods include: heteroscedasticity-consistent (HC) covariances for
	cross-section data; heteroscedasticity- and autocorrelation-consistent
	(HAC) covariances for time series data (such as Andrews' kernel HAC,
	Newey-West, and WEAVE estimators); clustered covariances (one-way and
	multi-way); panel and panel-corrected covariances;
	outer-product-of-gradients covariances; and (clustered) bootstrap
	covariances. All methods are applicable to (generalized) linear model
	objects fitted by lm() and glm() but can also be adapted to other classes
	through S3 methods. Details can be found in Zeileis et al. (2020)
	<doi:10.18637/jss.v095.i01>, Zeileis (2004) <doi:10.18637/jss.v011.i10> and
	Zeileis (2006) <doi:10.18637/jss.v016.i09>."""

	cran = "sandwich"

	license("GPL-2.0-only OR GPL-3.0-only")

	version("3.1-0", md5="a5abc91469c1f1ae604dba272268b10b")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
