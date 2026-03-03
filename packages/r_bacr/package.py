# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBacr(RPackage):
	"""Bayesian Adjustment for Confounding

	Estimating the average causal effect based on the Bayesian Adjustment for Confounding (BAC) algorithm.
	"""
	
	cran = "bacr" 

	version("1.0.1", md5="628d17d6f1a4a76dc1571ceb40fac999")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
