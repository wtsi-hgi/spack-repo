# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobustsae(RPackage):
	"""Robust Bayesian Small Area Estimation

	Functions for Robust Bayesian Small Area Estimation.
	"""
	
	cran = "robustsae" 

	version("0.1.0", md5="b4c22570af9b6c1e0cfa49fa2c306b47")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-pscl", type=("build", "run"))
