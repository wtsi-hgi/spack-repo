# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAspect(RPackage):
	"""A General Framework for Multivariate Analysis with Optimal
Scaling

	Contains various functions for optimal scaling. One function performs optimal scaling by maximizing an aspect (i.e. a target function such as the sum of eigenvalues, sum of squared correlations, squared multiple correlations, etc.) of the corresponding correlation matrix. Another function performs implements the LINEALS approach for optimal scaling by minimization of an aspect based on pairwise correlations and correlation ratios. The resulting correlation matrix and category scores can be used for further multivariate methods such as structural equation models. 
	"""
	
	homepage = "https://r-forge.r-project.org/projects/psychor/"
	cran = "aspect" 

	version("1.0-6", md5="a82463b308539e621fbd45983d5204ae")

	depends_on("r@3:", type=("build", "run"))
