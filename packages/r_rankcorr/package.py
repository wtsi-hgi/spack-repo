# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRankcorr(RPackage):
	"""Total, Between-, and Within-Cluster Spearman Rank Correlations
for Clustered Data

	Estimates the total, between-, and within-cluster Spearman rank correlations for continuous and ordinal clustered data. <https://github.com/shengxintu/rankCorr>.  
	"""
	
	cran = "rankCorr" 

	version("1.0.1", md5="5c2add3552187c94cab3ac301c924dbb")

	depends_on("r-rms@6.3:", type=("build", "run"))
	depends_on("r-rankicc@1.0.1:", type=("build", "run"))
