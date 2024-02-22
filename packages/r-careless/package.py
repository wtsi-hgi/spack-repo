# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCareless(RPackage):
	"""Procedures for Computing Indices of Careless Responding

	When taking online surveys, participants sometimes respond to items
    without regard to their content. These types of responses, referred to as 
    careless or insufficient effort responding, constitute significant problems 
    for data quality, leading to distortions in data analysis and hypothesis 
    testing, such as spurious correlations. The 'R' package 'careless' provides 
    solutions designed to detect such careless / insufficient effort responses 
    by allowing easy calculation of indices proposed in the literature. It 
    currently supports the calculation of longstring, even-odd consistency, 
    psychometric synonyms/antonyms, Mahalanobis distance, and intra-individual 
    response variability (also termed inter-item standard deviation). 
    For a review of these methods, see Curran (2016) <doi:10.1016/j.jesp.2015.07.006>.
	"""
	
	homepage = "https://github.com/ryentes/careless/"
	cran = "careless" 

	version("1.2.2", md5="088b2acc13af58c107af20e310031898")

	depends_on("r-psych", type=("build", "run"))
