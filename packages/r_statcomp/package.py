# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatcomp(RPackage):
	"""Statistical Complexity and Information Measures for Time Series
Analysis

	An implementation of local and global statistical complexity measures (aka Information Theory Quantifiers, ITQ) for time series analysis based on ordinal statistics (Bandt and Pompe (2002) <DOI:10.1103/PhysRevLett.88.174102>). Several distance measures that operate on ordinal pattern distributions, auxiliary functions for ordinal pattern analysis, and generating functions for stochastic and deterministic-chaotic processes for ITQ testing are provided. 
	"""
	
	cran = "statcomp" 

	version("0.1.0", md5="81e08320c024d68580f0a2448353c3f4")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
