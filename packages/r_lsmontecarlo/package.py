# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLsmontecarlo(RPackage):
	"""American options pricing with Least Squares Monte Carlo method

	The package compiles functions for calculating prices of American put options with Least Squares Monte Carlo method. The option types are plain vanilla American put, Asian American put, and Quanto American put. The pricing algorithms include variance reduction techniques such as Antithetic Variates and Control Variates. Additional functions are given to derive "price surfaces" at different volatilities and strikes, create 3-D plots, quickly generate Geometric Brownian motion, and calculate prices of European options with Black & Scholes analytical solution.
	"""
	
	cran = "LSMonteCarlo" 

	version("1.0", md5="7188e6a558eb0e642b5c1c1d628e4de5")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-fbasics", type=("build", "run"))
