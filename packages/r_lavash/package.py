# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLavash(RPackage):
	"""Lava Estimation for the Sum of Sparse and Dense Signals

	The lava estimation is a new technique to recover signals that is the sum of a sparse and dense signals. The post-lava method corrects the shrinkage bias of lava. For more information on the lava estimation, see Chernozhukov, Hansen, and Liao (2017) <doi:10.1214/16-AOS1434>.
	"""
	
	cran = "Lavash" 

	version("1.0", md5="67b22a4a2ee46e2d0f1d2e524f25c3b3")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
