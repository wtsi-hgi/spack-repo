# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRhierbaps(RPackage):
	"""Clustering Genetic Sequence Data Using the HierBAPS Algorithm

	Implements the hierarchical Bayesian analysis of populations structure (hierBAPS) 
  algorithm of Cheng et al. (2013) <doi:10.1093/molbev/mst028> for clustering DNA sequences 
  from multiple sequence alignments in FASTA format. 
  The implementation includes improved defaults and plotting capabilities 
  and unlike the original 'MATLAB' version removes singleton SNPs by default.
	"""
	
	homepage = "https://github.com/gtonkinhill/rhierbaps"
	cran = "rhierbaps" 

	version("1.1.4", md5="f29161b28806d58a2878c42f6990a1be")

	depends_on("r-ape", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
