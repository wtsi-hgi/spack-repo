# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJdmbs(RPackage):
	"""Monte Carlo Option Pricing Algorithms for Jump Diffusion Models
with Correlational Companies

	Option is a one of the financial derivatives and its pricing is an important problem in practice. The process of stock prices are represented as Geometric Brownian motion [Black (1973) <doi:10.1086/260062>] or jump diffusion processes [Kou (2002) <doi:10.1287/mnsc.48.8.1086.166>]. In this package, algorithms and visualizations are implemented by Monte Carlo method in order to calculate European option price for three equations by Geometric Brownian motion and jump diffusion processes and furthermore a model that presents jumps among companies affect each other.
	"""
	
	cran = "Jdmbs" 

	version("1.4", md5="0e2f1b113b20486af06575834dd97930")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
