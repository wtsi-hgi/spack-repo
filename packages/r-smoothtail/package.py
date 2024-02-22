# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmoothtail(RPackage):
	"""Smooth Estimation of GPD Shape Parameter

	Given independent and identically distributed observations X(1), ..., X(n) from a Generalized Pareto distribution with shape parameter gamma in [-1,0], offers several estimates to compute estimates of gamma. The estimates are based on the principle of replacing the order statistics by quantiles of a distribution function based on a log--concave density function. This procedure is justified by the fact that the GPD density is log--concave for gamma in [-1,0].
	"""
	
	homepage = "http://www.kasparrufibach.ch"
	cran = "smoothtail" 

	version("2.0.5", md5="e5b5d29f2ca719dfca06c745818e51a9")

	depends_on("r-logcondens@2:", type=("build", "run"))
