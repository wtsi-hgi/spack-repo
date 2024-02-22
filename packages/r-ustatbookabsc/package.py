# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUstatbookabsc(RPackage):
	"""A Companion Package to the Book "U-Statistics, M-Estimation and
Resampling"

	A set of functions leading to multivariate response L1 regression. 
    This includes functions on computing Euclidean inner products and norms, 
    weighted least squares estimates on multivariate responses, function to compute 
    fitted values and residuals. This package is a companion to the book "U-Statistics,
    M-estimation and Resampling", by Arup Bose and Snigdhansu Chatterjee, to appear 
    in 2017 as part of the "Texts and Readings in Mathematics" (TRIM) series of 
    Hindustan Book Agency and Springer-Verlag.
	"""
	
	cran = "UStatBookABSC" 

	version("1.0.0", md5="868901c53ff9dc6fac050d4db287386f")

	depends_on("r@3.2.3:", type=("build", "run"))
