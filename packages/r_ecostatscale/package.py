# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcostatscale(RPackage):
	"""Statistical Scaling Functions for Ecological Systems

	Implementation of the scaling functions presented in "General statistical scaling laws for stability in ecological systems" by Clark et al in Ecology Letters <DOI:10.1111/ele.13760>. Includes functions for extrapolating variability, resistance, and resilience across spatial and ecological scales, as well as a basic simulation function for producing time series, and a regression routine for generating unbiased parameter estimates. See the main text of the paper for more details.
	"""
	
	cran = "ecostatscale" 

	version("1.1", md5="2ce0a2fb7475f5827663ac67ef1d7c36")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
