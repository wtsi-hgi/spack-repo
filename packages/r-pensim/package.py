# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPensim(RPackage):
	"""Simulation of High-Dimensional Data and Parallelized Repeated
Penalized Regression

	Simulation of continuous, correlated high-dimensional data with 
    time to event or binary response, and parallelized functions for Lasso, 
    Ridge, and Elastic Net penalized regression with repeated starts and 
    two-dimensional tuning of the Elastic Net.
	"""
	
	homepage = "https://waldronlab.io/pensim/"
	cran = "pensim" 

	version("1.3.6", md5="4e0ce82f493302a095afa1644d04d5d7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-penalized", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
