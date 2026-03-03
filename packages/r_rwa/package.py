# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRwa(RPackage):
	"""Perform a Relative Weights Analysis

	Perform a Relative Weights Analysis (RWA) (a.k.a. Key Drivers Analysis) as per the method described 
    in Tonidandel & LeBreton (2015) <DOI:10.1007/s10869-014-9351-z>, with its original roots in Johnson (2000) <DOI:10.1207/S15327906MBR3501_1>. In essence, RWA decomposes
    the total variance predicted in a regression model into weights that accurately reflect the proportional 
    contribution of the predictor variables, which addresses the issue of multi-collinearity. In typical scenarios,
    RWA returns similar results to Shapley regression, but with a significant advantage on computational performance.
	"""
	
	homepage = "https://github.com/martinctc/rwa"
	cran = "rwa" 

	version("0.0.3", md5="e23fbbc808a89b82306c859fde1ad61c")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
