# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROcomposition(RPackage):
	"""Regression for Rank-Indexed Compositional Data

	Regression model where the response variable is a rank-indexed compositional vector (non-negative values that sum up to one and are ordered from the largest to the smallest). Parameters are estimated in the Bayesian framework using MCMC methods. 
	"""
	
	cran = "ocomposition" 

	version("1.1", md5="fd1ea6bd7746b37c756328243cc84ec7")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-bayesm", type=("build", "run"))
