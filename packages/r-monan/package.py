# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMonan(RPackage):
	"""Mobility Network Analysis

	Implements the method to analyse weighted mobility networks or distribution networks as outlined in: 
    Block, P., Stadtfeld, C., & Robins, G. (2022) <doi:10.1016/j.socnet.2021.08.003>. 
    The purpose of the model is to analyse the structure of mobility, 
    incorporating exogenous predictors pertaining to individuals and locations 
    known from classical mobility analyses, as well as modelling emergent mobility 
    patterns akin to structural patterns known from the statistical analysis of social networks.
	"""
	
	cran = "MoNAn" 

	version("0.1.3", md5="c40df2d0167a7256d124810ecc873a59")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-snowfall@1.84.6.2:", type=("build", "run"))
