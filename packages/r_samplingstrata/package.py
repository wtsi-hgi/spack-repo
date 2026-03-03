# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSamplingstrata(RPackage):
	"""Optimal Stratification of Sampling Frames for Multipurpose
Sampling Surveys

	In the field of stratified sampling design, this package offers an approach for the determination of the best stratification of a sampling frame, the one that ensures the minimum sample cost under the condition to satisfy precision constraints in a multivariate and multidomain case. This approach is based on the use of the genetic algorithm: each solution (i.e. a particular partition in strata of the sampling frame) is considered as an individual in a population; the fitness of all individuals is evaluated applying the Bethel-Chromy algorithm to calculate the sampling size satisfying precision constraints on the target estimates. Functions in the package allows to: (a) analyse the obtained results of the optimisation step; (b) assign the new strata labels to the sampling frame; (c) select a sample from the new frame accordingly to the best allocation. Functions for the execution of the genetic algorithm are a modified version of the functions in the 'genalg' package. M.Ballin, G.Barcaroli (2020) <arXiv:2004.09366> "R package SamplingStrata: new developments and extension to Spatial Sampling".  
	"""
	
	homepage = "https://barcaroli.github.io/SamplingStrata/"
	cran = "SamplingStrata" 

	version("1.5-4", md5="d4c34526fc638087d1fef3e6921f5ccf")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-samplingbigdata", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
