# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArMatrix(RPackage):
	"""Simulate Auto Regressive Data from Precision Matricies

	Using sparse precision matricies and Choleski factorization simulates data that is auto-regressive.
	"""
	
	cran = "ar.matrix" 

	version("0.1.0", md5="be61d91fcb464b1b3628837ab88e25e9")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-sparsemvn", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
