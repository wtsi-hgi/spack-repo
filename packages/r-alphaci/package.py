# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlphaci(RPackage):
	"""Confidence Intervals for Coefficient Alpha and Standardized
Alpha

	Calculate confidence intervals for alpha and standardized
    alpha using asymptotic theory or the studentized bootstrap, with or
    without transformations. Supports the asymptotic distribution-free
    method of Maydeu-Olivares, et al. (2007)
    <doi:10.1037/1082-989X.12.2.157>, the pseudo-elliptical method of Yuan
    & Bentler (2002) <doi:10.1007/BF02294845>, and the normal method of
    van Zyl et al. (1999) <doi:10.1007/BF02296146>, for both coefficient
    alpha and standardized alpha.
	"""
	
	homepage = "https://jonasmoss.github.io/alphaci/"
	cran = "alphaci" 

	version("1.0.1", md5="7924b96ce4706ff488e23f8b8f21035c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
