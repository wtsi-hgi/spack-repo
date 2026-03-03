# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCascore(RPackage):
	"""Covariate Assisted Spectral Clustering on Ratios of Eigenvectors

	Functions for implementing the novel algorithm CASCORE, which is designed to detect latent community structure in graphs with node covariates. This algorithm can handle models such as the covariate-assisted degree corrected stochastic block model (CADCSBM). CASCORE specifically addresses the disagreement between the community structure inferred from the adjacency information and the community structure inferred from the covariate information. For more detailed information, please refer to the reference paper: Yaofang Hu and Wanjie Wang (2022) <arXiv:2306.15616>. 
    In addition to CASCORE, this package includes several classical community detection algorithms that are compared to CASCORE in our paper. These algorithms are: Spectral Clustering On Ratios-of Eigenvectors (SCORE), normalized PCA, ordinary PCA, network-based clustering, covariates-based clustering and covariate-assisted spectral clustering (CASC). By providing these additional algorithms, the package enables users to compare their performance with CASCORE in community detection tasks.
	"""
	
	homepage = "https://arxiv.org/abs/2306.15616"
	cran = "CASCORE" 

	version("0.1.2", md5="c37a1d52176577adc3f440146fce0027")

	depends_on("r-pracma", type=("build", "run"))
