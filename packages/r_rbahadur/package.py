# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbahadur(RPackage):
	"""Assortative Mating Simulation and Multivariate Bernoulli
Variates

	Simulation of phenotype / genotype data under assortative mating. 
    Includes functions for generating Bahadur order-2 multivariate Bernoulli 
    variables with general and diagonal-plus-low-rank correlation structures. 
    Further details are provided in: Border and Malik (2022) 
    <doi:10.1101/2022.10.13.512132>.
	"""
	
	homepage = "https://github.com/rborder/rBahadur"
	cran = "rBahadur" 

	version("1.0.0", md5="33f6655a04208c96a5086351a955c13a")

	depends_on("r@3.3:", type=("build", "run"))
