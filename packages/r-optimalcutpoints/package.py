# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptimalcutpoints(RPackage):
	"""Computing Optimal Cutpoints in Diagnostic Tests

	Computes optimal cutpoints for diagnostic tests or continuous markers. Various approaches for selecting optimal cutoffs have been implemented, including methods based on cost-benefit analysis and diagnostic test accuracy measures (Sensitivity/Specificity, Predictive Values and Diagnostic Likelihood Ratios). Numerical and graphical output for all methods is easily obtained.
	"""
	
	cran = "OptimalCutpoints" 

	version("1.1-5", md5="8d4e1973050c9ab5fa43d024fe2c147b")

