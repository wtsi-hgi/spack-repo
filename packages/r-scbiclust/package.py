# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScbiclust(RPackage):
	"""Identifies Mean, Variance, and Hierarchically Clustered
Biclusters

	Identifies a bicluster, a submatrix of the data such that the features and observations within the submatrix differ from those not contained in submatrix, using a two-step method. In the first step, observations in the bicluster are  identified to maximize the sum of weighted between cluster feature differences. The method is described in Helgeson et al. (2020) <doi:10.1111/biom.13136>. 'SCBiclust' can be used to identify biclusters which differ based on feature means, feature variances, or more general differences. 
	"""
	
	cran = "SCBiclust" 

	version("1.0.1", md5="f1cbfc9ad3784b566ba480151fae12fb")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-sparcl", type=("build", "run"))
	depends_on("r-sigclust", type=("build", "run"))
