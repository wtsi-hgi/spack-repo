# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixghd(RPackage):
	"""Model Based Clustering, Classification and Discriminant Analysis
Using the Mixture of Generalized Hyperbolic Distributions

	Carries out model-based clustering, classification and discriminant analysis using five different models. The models are all based on the  generalized hyperbolic distribution. The first model 'MGHD' (Browne and McNicholas (2015) <doi:10.1002/cjs.11246>) is the classical mixture of generalized hyperbolic distributions. The 'MGHFA' (Tortora et al. (2016) <doi:10.1007/s11634-015-0204-z>) is the mixture of generalized hyperbolic factor analyzers for high dimensional data sets. The 'MSGHD' is the mixture of  multiple scaled generalized hyperbolic distributions, the 'cMSGHD'  is a 'MSGHD' with convex contour plots and the 'MCGHD', mixture of  coalesced generalized hyperbolic distributions is a new more flexible model (Tortora et al. (2019)<doi:10.1007/s00357-019-09319-3>. The paper related to the software can be found at <doi:10.18637/jss.v098.i03>.
	"""
	
	cran = "MixGHD" 

	version("2.3.7", md5="2bca4ceb689debc9caac1ca22637d3e3")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r@3.1.3:", type=("build", "run"))
	depends_on("r-bessel", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-ghyp", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-mixture", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
