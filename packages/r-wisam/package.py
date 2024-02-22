# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWisam(RPackage):
	"""Weighted Inbred Strain Association Mapping

	In the course of a genome-wide association study, the situation often arises that some phenotypes are known with greater precision than others.
    It could be that some individuals are known to harbor more micro-environmental variance than others.
    In the case of inbred strains of model organisms, it could be the case that more organisms were observed from some strains than others, so the strains with more organisms have better-estimated means.
    Package 'wISAM' handles this situation by allowing for weighting of each observation according to residual variance.
    Specifically, the 'weight' parameter to the function conduct_scan() takes the precision of each observation (one over the variance). 
	"""
	
	cran = "wISAM" 

	version("0.2.8", md5="a3bb289ab495eff9e3e89812728ad364")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
