# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatching(RPackage):
	"""Multivariate and Propensity Score Matching with Balance
Optimization

	Provides functions for multivariate and propensity score matching 
             and for finding optimal balance based on a genetic search algorithm. 
             A variety of univariate and multivariate metrics to
             determine if balance has been obtained are also provided. For
             details, see the paper by Jasjeet Sekhon 
             (2007, <doi:10.18637/jss.v042.i07>).
	"""
	
	homepage = "https://github.com/JasjeetSekhon/Matching"
	cran = "Matching" 

	version("4.10-14", md5="c7cff83f8723c0f24c2c985a3a776ac7")
	version("4.10-8", md5="9f0438193baa073b42266c49a24b1502")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-mass@7.2.1:", type=("build", "run"))
