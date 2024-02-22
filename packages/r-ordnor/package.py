# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrdnor(RPackage):
	"""Concurrent Generation of Ordinal and Normal Data with Given
Correlation Matrix and Marginal Distributions

	Implementation of a procedure for generating samples from a mixed distribution of ordinal and normal random variables with a pre-specified correlation matrix and marginal distributions.
             The details of the method are explained in Demirtas et al. (2015) <DOI:10.1080/10543406.2014.920868>.
	"""
	
	cran = "OrdNor" 

	version("2.2.3", md5="01f5bb2faed203f273dfe197c88755d5")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-genord", type=("build", "run"))
