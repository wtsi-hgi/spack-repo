# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcmc4extremes(RPackage):
	"""Posterior Distribution of Extreme Value Models in R

	Provides some function to perform posterior estimation for some distribution, with emphasis to extreme value distributions. It contains some extreme datasets, and functions that perform the runs of posterior points of the GPD and GEV distribution. The package calculate some important extreme measures like return level for each t periods of time, and some plots as the predictive distribution, and return level plots. 
	"""
	
	cran = "MCMC4Extremes" 

	version("1.1", md5="0536c1f6bae32ac5374833875dd5c15f")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-evir", type=("build", "run"))
