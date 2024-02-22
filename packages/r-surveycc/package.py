# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurveycc(RPackage):
	"""Canonical Correlation for Survey Data

	Performs canonical correlation for survey data, including 
  multiple tests of significance for secondary canonical correlations. 
  A key feature of this package is that it incorporates survey data structure 
  directly in a novel test of significance via a sequence of simple linear 
  regression models on the canonical variates. See reference - Cruz-Cano, 
  Cohen, and Mead-Morse (2024) "Canonical Correlation Analysis of Survey data: the SurveyCC R package" 
  The R Journal under review.
	"""
	
	cran = "SurveyCC" 

	version("0.1.1", md5="a202407fab638e9485375c07f9742c1b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-candisc", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
