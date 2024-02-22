# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBinomialrf(RPackage):
	"""Binomial Random Forest Feature Selection

	The 'binomialRF' is a new feature selection technique for decision trees that aims at providing an alternative approach to identify significant feature subsets using binomial distributional assumptions (Rachid Zaim, S., et al. (2019)) <doi:10.1101/681973>. Treating each splitting variable selection as a set of exchangeable correlated Bernoulli trials, 'binomialRF' then tests whether a feature is selected more often than by random chance. 
	"""
	
	homepage = "https://www.biorxiv.org/content/10.1101/681973v1.abstract"
	cran = "binomialRF" 

	version("0.1.0", md5="2d646c1f58a0f46c30f19ba25d50973b")

	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
