# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAldqr(RPackage):
	"""Quantile Regression Using Asymmetric Laplace Distribution

	EM algorithm for estimation of parameters and other methods in a quantile regression. 
	"""
	
	cran = "ALDqr" 

	version("1.0", md5="c43401b9682152bb77ecc0ad0a5c12af")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-hyperbolicdist", type=("build", "run"))
	depends_on("r-sn", type=("build", "run"))
