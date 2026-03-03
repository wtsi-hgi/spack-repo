# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBivrec(RPackage):
	"""Bivariate Alternating Recurrent Event Data Analysis

	A collection of models for bivariate alternating recurrent event data analysis. 
             Includes non-parametric and semi-parametric methods.
	"""
	
	homepage = "https://github.com/SandraCastroPearson/BivRec"
	cran = "BivRec" 

	version("1.2.1", md5="763d4b6b4afca64255c49a46e9929bb5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
