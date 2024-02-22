# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVariability(RPackage):
	"""Genetic Variability Analysis for Plant Breeding Research

	Performs analysis of various genetic parameters like genotypic and phenotypic coefficient of variance, heritability, genetic advance, genetic advance as a percentage of mean. The package also has functions for genotypic and phenotypic covariance, correlation and path analysis. Dataset has been added to facilitate example. For more information refer Singh, R.K. and Chaudhary, B.D. (1977, ISBN:81766330709788176633079).
	"""
	
	cran = "variability" 

	version("0.1.0", md5="4b26aa32187e087c069a512ea7e6a308")

	depends_on("r@2.10:", type=("build", "run"))
