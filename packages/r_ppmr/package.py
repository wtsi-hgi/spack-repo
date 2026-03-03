# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPpmr(RPackage):
	"""Probabilistic Two Sample Mendelian Randomization

	Efficient statistical inference of two-sample MR (Mendelian Randomization) analysis. 
    It can account for the correlated instruments and the horizontal pleiotropy, 
    and can provide the accurate estimates of both causal effect and horizontal 
    pleiotropy effect as well as the two corresponding p-values. There are two main 
    functions in the 'PPMR' package. One is PMR_individual() for individual level data, 
    the other is PMR_summary() for summary data.
	"""
	
	cran = "PPMR" 

	version("1.0", md5="89ece2cfe65ee10b466a491e518f15cd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
