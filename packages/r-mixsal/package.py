# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixsal(RPackage):
	"""Mixtures of Multivariate Shifted Asymmetric Laplace (SAL)
Distributions

	The current version of the 'MixSAL' package allows users to generate data from a multivariate SAL distribution or a mixture of multivariate SAL distributions, evaluate the probability density function of a multivariate SAL distribution or a mixture of multivariate SAL distributions, and fit a mixture of multivariate SAL distributions using the Expectation-Maximization (EM) algorithm (see Franczak et. al, 2014, <doi:10.1109/TPAMI.2013.216>, for details). 
	"""
	
	cran = "MixSAL" 

	version("1.0", md5="e879c05102b711d9ab6b9273cd99f212")

	depends_on("r-mass@3.1.3:", type=("build", "run"))
