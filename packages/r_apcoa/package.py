# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApcoa(RPackage):
	"""Covariate Adjusted PCoA Plot

	In fields such as ecology, microbiology, and genomics, non-Euclidean distances are widely applied to describe pairwise dissimilarity between samples. Given these pairwise distances, principal coordinates analysis (PCoA) is commonly used to construct a visualization of the data. However, confounding covariates can make patterns related to the scientific question of interest difficult to observe. We provide 'aPCoA' as an easy-to-use tool to improve data visualization in this context, enabling enhanced presentation of the effects of interest. Details are described in Yushu Shi, Liangliang Zhang, Kim-Anh Do, Christine Peterson and Robert Jenq (2020) Bioinformatics, Volume 36, Issue 13, 4099-4101.
	"""
	
	cran = "aPCoA" 

	version("1.3", md5="7b8bc767445800ddb03980f0cce2162b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-randomcolor", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
