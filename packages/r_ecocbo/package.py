# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcocbo(RPackage):
	"""Calculating Optimum Sampling Effort in Community Ecology

	A system for calculating the optimal sampling effort, based on the ideas of 
    "Ecological cost-benefit optimization" as developed by A. Underwood (1997, 
    ISBN 0 521 55696 1). Data is obtained from simulated ecological communities, 
    and the optimization follows the following procedure of four functions (1) 
    sim_beta() estimates statistical power and type 2 error by using Permutational 
    Multivariate Analysis of Variance, (2) plot_power() represents the results 
    of the previous function, (3) scompvar() calculates the variation components 
    necessary for (4) sim_cbo() to calculate the optimal combination of number 
    of sites and samples depending on either an economical budget or on a desired 
    statistical accuracy. 
	"""
	
	cran = "ecocbo" 

	version("0.10.2", md5="19ff292ca4111f0b332b9eaefa7cf84c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-sampling", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
