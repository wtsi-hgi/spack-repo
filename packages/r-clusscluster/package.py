# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClusscluster(RPackage):
	"""Simultaneous Detection of Clusters and Cluster-Specific Genes in
High-Throughput Transcriptome Data

	Implements a new method 'ClussCluster' descried in Ge Jiang and Jun Li, "Simultaneous Detection of Clusters and Cluster-Specific Genes in High-throughput Transcriptome Data" (Unpublished).
	Simultaneously perform clustering analysis and signature 	gene selection on high-dimensional transcriptome data sets. 	To do so, 'ClussCluster' incorporates a Lasso-type 	regularization penalty term to the objective function of K-	means so that cell-type-specific signature genes can be 	identified while clustering the cells.
	"""
	
	cran = "ClussCluster" 

	version("0.1.0", md5="5c252830d5f4a8afa114f0a97268e8a6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-venndiagram", type=("build", "run"))
	depends_on("r-scales@1:", type=("build", "run"))
	depends_on("r-reshape2@1.4.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-rlang@0.3.4:", type=("build", "run"))
