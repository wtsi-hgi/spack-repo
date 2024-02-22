# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPriorgen(RPackage):
	"""Generates Prior Distributions for Proportions

	
  Translates beliefs into prior information in the form of Beta and Gamma distributions. 
	It can be used for the generation of priors on the prevalence of disease and 
	the sensitivity/specificity of diagnostic tests and any other binomial experiment.
	"""
	
	cran = "PriorGen" 

	version("2.0", md5="69ba0e696e96d5ca42549872f86f5bab")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
