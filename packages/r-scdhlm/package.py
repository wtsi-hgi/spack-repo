# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScdhlm(RPackage):
	"""Estimating Hierarchical Linear Models for Single-Case Designs

	Provides a set of tools for estimating hierarchical linear
    models and effect sizes based on data from single-case designs. 
    Functions are provided for calculating standardized mean difference effect sizes that 
    are directly comparable to standardized mean differences estimated from between-subjects randomized experiments,
    as described in Hedges, Pustejovsky, and Shadish (2012) <DOI:10.1002/jrsm.1052>; 
    Hedges, Pustejovsky, and Shadish (2013) <DOI:10.1002/jrsm.1086>; 
    Pustejovsky, Hedges, and Shadish (2014) <DOI:10.3102/1076998614547577>; 
    and Chen, Pustejovsky, Klingbeil, and Van Norman (2023) <DOI:10.1016/j.jsp.2023.02.002>. 
    Includes an interactive web interface.
	"""
	
	homepage = "https://jepusto.github.io/scdhlm/"
	cran = "scdhlm" 

	version("0.7.3", md5="d21c76194ab9a6b60dd09664cc274a5e")

	depends_on("r-nlme", type=("build", "run"))
	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-lmeinfo@0.3:", type=("build", "run"))
