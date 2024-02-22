# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShuffle(RPackage):
	"""The Shuffle Estimator for Explainable Variance

	Implementation of the shuffle estimator, a non-parametric estimator for signal and noise variance under mild noise correlations.  
	"""
	
	cran = "shuffle" 

	version("1.0.1", md5="4dcce63a83b8be92195c4d27a4e71bb6")

