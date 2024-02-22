# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBetapass(RPackage):
	"""Calculate Power and Sample Size with Beta Regression

	Power calculations are a critical component of any research study to determine the 
	minimum sample size necessary to detect differences between multiple groups. 
	Researchers often work with data taking the form of proportions that can be modeled with 
	a beta distribution. Here we present an R package, 'BetaPASS', that perform power and 
	sample size calculations for data following a beta distribution with comparative 
	nonparametric output. This package allows flexibility with multiple options for link 
	functions to fit the data and graphing functionality for visual comparisons.
	"""
	
	cran = "BetaPASS" 

	version("1.1-2", md5="44bf3f6262822149ef907d93c43b0faa")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-betareg", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
