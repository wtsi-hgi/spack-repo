# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBshazard(RPackage):
	"""Nonparametric Smoothing of the Hazard Function

	The function estimates the hazard function non parametrically 
	     from a survival object (possibly adjusted for covariates). 
	     The smoothed estimate is based on B-splines from the perspective 
	     of generalized linear mixed models. Left truncated 
	     and right censoring data are allowed.
	"""
	
	cran = "bshazard" 

	version("1.1", md5="a5b7a0ac819c425735c942ebca86f08e")

	depends_on("r@3.3.3:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-epi", type=("build", "run"))
