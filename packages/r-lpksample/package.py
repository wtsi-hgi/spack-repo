# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLpksample(RPackage):
	"""LP Nonparametric High Dimensional K-Sample Comparison

	LP nonparametric high-dimensional K-sample comparison method that includes 
    (i) confirmatory test, (ii) exploratory analysis, and (iii) options to output a 
	data-driven LP-transformed matrix for classification. The primary reference is 
	Mukhopadhyay, S. and Wang, K. (2020, Biometrika); <arXiv:1810.01724>.
	"""
	
	cran = "LPKsample" 

	version("2.1", md5="0fc44af832108957e85fa1bad25bc9ff")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-apcluster", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-lpgraph", type=("build", "run"))
