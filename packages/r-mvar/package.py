# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvar(RPackage):
	"""Multivariate Analysis

	Package for multivariate analysis, having functions that perform simple correspondence analysis (CA) and multiple correspondence analysis (MCA), principal components analysis (PCA), canonical correlation analysis (CCA), factorial analysis (FA), multidimensional scaling (MDS), linear (LDA) and quadratic discriminant analysis (QDA), hierarchical and non-hierarchical cluster analysis, simple and multiple linear regression, multiple factor analysis (MFA) for quantitative, qualitative, frequency (MFACT) and mixed data, biplot, scatter plot, projection pursuit (PP), grant tour method and other useful functions for the multivariate analysis.
	"""
	
	cran = "MVar" 

	version("2.2.1", md5="dbeace1fa6e4dee05bedea5c3c5ee9f7")

	depends_on("r-mass", type=("build", "run"))
