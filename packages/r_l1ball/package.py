# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RL1ball(RPackage):
	"""L1-Ball Prior for Sparse Regression

	Provides function for the l1-ball prior on high-dimensional regression. The main function, l1ball(), yields posterior samples for linear regression, as introduced by Xu and Duan (2020) <arXiv:2006.01340>.
	"""
	
	cran = "l1ball" 

	version("0.1.0", md5="3dbab6f4ca79f79909180e95c1550377")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
