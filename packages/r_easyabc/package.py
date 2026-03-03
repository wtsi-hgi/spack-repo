# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REasyabc(RPackage):
	"""Efficient Approximate Bayesian Computation Sampling Schemes

	Enables launching a series of simulations of a computer code from the R session, and to retrieve the simulation outputs in an appropriate format for post-processing treatments. Five sequential sampling schemes and three coupled-to-MCMC schemes are implemented.
	"""
	
	homepage = "http://easyabc.r-forge.r-project.org/"
	cran = "EasyABC" 

	version("1.5.2", md5="80af9a802cd4799c90cb9be08b3b9b94")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-abc", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lhs", type=("build", "run"))
	depends_on("r-tensora", type=("build", "run"))
