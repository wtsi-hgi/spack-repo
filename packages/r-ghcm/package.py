# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGhcm(RPackage):
	"""Functional Conditional Independence Testing with the GHCM

	A statistical hypothesis test for conditional independence.
    Given residuals from a sufficiently powerful regression, it tests whether 
    the covariance of the residuals is vanishing. It can be applied to both
    discretely-observed functional data and multivariate data. 
    Details of the method can be found in Anton Rask Lundborg, Rajen D. Shah and Jonas
    Peters (2022) <doi:10.1111/rssb.12544>.
	"""
	
	homepage = "https://github.com/arlundborg/ghcm"
	cran = "ghcm" 

	version("3.0.1", md5="b32510ae4f841023a816f1e3334b67c3")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
