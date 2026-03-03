# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNac(RPackage):
	"""Network-Adjusted Covariates for Community Detection

	Incorporating node-level covariates for community detection has gained increasing attention these years. This package provides the function for implementing the novel community detection algorithm known as Network-Adjusted Covariates for Community Detection (NAC), which is designed to detect latent community structure in graphs with node-level information, i.e., covariates. This algorithm can handle models such as the degree-corrected stochastic block model (DCSBM) with covariates. NAC specifically addresses the discrepancy between the community structure inferred from the adjacency information and the community structure inferred from the covariates information. For more detailed information, please refer to the reference paper: Yaofang Hu and Wanjie Wang (2023) <arXiv:2306.15616>. In addition to NAC, this package includes several other existing community detection algorithms that are compared to NAC in the reference paper. These algorithms are Spectral Clustering On Ratios-of Eigenvectors (SCORE), network-based regularized spectral clustering (Net-based), covariate-based spectral clustering (Cov-based), covariate-assisted spectral clustering (CAclustering) and semidefinite programming (SDP). 
	"""
	
	homepage = "https://arxiv.org/abs/2306.15616"
	cran = "NAC" 

	version("0.1.0", md5="ee430d1142b486235b1e8997c4a0977e")

	depends_on("r@4.2.2:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
