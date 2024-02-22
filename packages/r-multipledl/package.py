# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultipledl(RPackage):
	"""Addressing Detection Limits by Cumulative Probability Models
(CPMs)

	Build CPMs (cumulative probability models, also known as cumulative link models) to account for detection limits (both single and multiple detection limits) in response variables. Conditional quantiles and conditional CDFs can be calculated based on fitted models. The package implements methods described in Tian, Y., Li, C., Tu, S., James, N. T., Harrell, F. E., & Shepherd, B. E. (2022). "Addressing Detection Limits with Semiparametric Cumulative Probability Models". <arXiv:2207.02815>.
	"""
	
	cran = "multipleDL" 

	version("1.0.0", md5="f7dbc3f9673b498b8172c88d32def385")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-rstantools@2.1.1:", type=("build", "run"))
	depends_on("r-sparsem", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
