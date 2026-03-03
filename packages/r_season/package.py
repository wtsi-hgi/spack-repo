# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeason(RPackage):
	"""Seasonal Analysis of Health Data

	Routines for the seasonal analysis of health data, including regression models, time-stratified case-crossover, plotting functions and residual checks, see Barnett and Dobson (2010) ISBN 978-3-642-10748-1. Thanks to Yuming Guo for checking the case-crossover code. 
	"""
	
	cran = "season" 

	version("0.3.15", md5="22a5c0b0e246fb5651b93d59fa34e55e")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-ggplot2@0.9.3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
