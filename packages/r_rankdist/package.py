# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRankdist(RPackage):
	"""Distance Based Ranking Models

	Implements distance based probability models for ranking data. 
    The supported distance metrics include Kendall distance, Spearman distance, Footrule distance, Hamming distance,
    Weighted-tau distance and Weighted Kendall distance.
    Phi-component model and mixture models are also supported.
	"""
	
	cran = "rankdist" 

	version("1.1.4", md5="865cf123628ae38b543b49de2fbb6a0d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-hash", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-permute", type=("build", "run"))
