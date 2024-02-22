# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REummd(RPackage):
	"""Efficient Univariate Maximum Mean Discrepancy

	Computes maximum mean discrepancy two-sample test for univariate data using the Laplacian kernel, as described in Bodenham and Kawahara (2023) <doi:10.1007/s11222-023-10271-x>. The p-value is computed using permutations. Also includes implementation for computing the robust median difference statistic 'Q_n' from Croux and Rousseeuw (1992) <doi:10.1007/978-3-662-26811-7_58> based on Johnson and Mizoguchi (1978) <doi:10.1137/0207013>. 
	"""
	
	cran = "eummd" 

	version("0.1.4", md5="6f7530cce144df75e84597677a9e40b3")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
