# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImix(RPackage):
	"""Gaussian Mixture Model for Multi-Omics Data Integration

	A multivariate Gaussian mixture model framework to integrate multiple types of genomic data and allow modeling of inter-data-type correlations for association analysis. 'IMIX' can be implemented to test whether a disease is associated with genes in multiple genomic data types, such as DNA methylation, copy number variation, gene expression, etc. It can also study the integration of multiple pathways. 'IMIX' uses the summary statistics of association test outputs and conduct integration analysis for two or three types of genomics data. 'IMIX' features statistically-principled model selection, global FDR control and computational efficiency. Details are described in Ziqiao Wang and Peng Wei (2020) <doi:10.1093/bioinformatics/btaa1001>. 
	"""
	
	homepage = "https://github.com/ziqiaow/IMIX"
	cran = "IMIX" 

	version("1.1.5", md5="0c396114b8fb44cc768701814e71ff22")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mixtools", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
