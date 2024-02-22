# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSenstrat(RPackage):
	"""Sensitivity Analysis for Stratified Observational Studies

	Sensitivity analysis in unmatched observational studies, with or without strata.  The main functions are sen2sample() and senstrat().  See Rosenbaum, P. R. and Krieger, A. M. (1990), JASA, 85, 493-498, <doi:10.1080/01621459.1990.10476226> and Gastwirth, Krieger and Rosenbaum (2000), JRSS-B, 62, 545–555 <doi:10.1111/1467-9868.00249> .
	"""
	
	cran = "senstrat" 

	version("1.0.3", md5="7726bcd949e484c78be2dea6aba43f21")

	depends_on("r-biasedurn", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
