# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZinar1(RPackage):
	"""Simulates ZINAR(1) Model and Estimates Its Parameters Under
Frequentist Approach

	Generates Realizations of First-Order Integer Valued Autoregressive Processes with Zero-Inflated Innovations (ZINAR(1)) and Estimates its Parameters as described in Garay et al. (2021) <doi:10.1007/978-3-030-82110-4_2>.
	"""
	
	cran = "ZINAR1" 

	version("0.1.0", md5="255a1a44e3da982eb3ba4b78d94826fb", url="https://cran.r-project.org/src/contrib/ZINAR1_0.1.0.tar.gz")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-gamlss-dist", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
