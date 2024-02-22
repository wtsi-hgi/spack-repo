# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMontecarlo(RPackage):
	"""Automatic Parallelized Monte Carlo Simulations

	Simplifies Monte Carlo simulation studies by automatically 
             setting up loops to run over parameter grids and parallelising
             the Monte Carlo repetitions. It also generates LaTeX tables.
	"""
	
	homepage = "http://github.com/FunWithR/MonteCarlo"
	cran = "MonteCarlo" 

	version("1.0.6", md5="04c18ab996031530a903c37f6b618925")

	depends_on("r-snow@0.4.1:", type=("build", "run"))
	depends_on("r-abind@1.4.0:", type=("build", "run"))
	depends_on("r-codetools@0.2.8:", type=("build", "run"))
	depends_on("r-rlecuyer@0.3.4:", type=("build", "run"))
	depends_on("r-snowfall@1.84.4:", type=("build", "run"))
	depends_on("r-reshape@0.8.6:", type=("build", "run"))
