# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvlong(RPackage):
	"""Analysis of Proportional Hazards Model with Sparse Longitudinal
Covariates

	Provides kernel weighting methods for estimation of proportional 
    hazards models with intermittently observed longitudinal covariates. 
    Cao H., Churpek M. M., Zeng D., and Fine J. P. (2015) 
    <doi:10.1080/01621459.2014.957289>.
	"""
	
	cran = "SurvLong" 

	version("1.4", md5="b7a5f64b6d025434196df58a23af11e4")

