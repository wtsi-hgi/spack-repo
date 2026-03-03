# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCauchypca(RPackage):
	"""Robust Principal Component Analysis Using the Cauchy
Distribution

	A new robust principal component analysis algorithm is implemented that relies upon the Cauchy Distribution. The algorithm is suitable for high dimensional data even if the sample size is less than the number of variables. The methodology is described in this paper: Fayomi A., Pantazis Y., Tsagris M. and Wood A.T.A. (2024). "Cauchy robust principal component analysis with applications to high-dimensional data sets". Statistics and Computing, 34: 26. <doi:10.1007/s11222-023-10328-x>.
	"""
	
	cran = "cauchypca" 

	version("1.3", md5="5e819a3b7606390586a4b0b421ec8827")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-rfast2", type=("build", "run"))
