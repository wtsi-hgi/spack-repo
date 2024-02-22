# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpadmixture(RPackage):
	"""Iterative Pruning Population Admixture Inference Framework

	A data clustering package based on admixture ratios (Q matrix) of population structure. The framework is based on iterative Pruning procedure that performs data clustering by splitting a given population into subclusters until meeting the condition of stopping criteria the same as ipPCA, iNJclust, and IPCAPS frameworks. The package also provides a function to retrieve phylogeny tree that construct a neighbor-joining tree based on a similar matrix between clusters. By given multiple Q matrices with varying a number of ancestors (K), the framework define a similar value between clusters i,j as a minimum number K* that makes majority of members of two clusters are in the different clusters. This K* reflexes a minimum number of ancestors we need to splitting cluster i,j into different clusters if we assign K* clusters based on maximum admixture ratio of individuals. The publication of this package is at Chainarong Amornbunchornvej, Pongsakorn Wangkumhang, and Sissades Tongsima (2020) <doi:10.1101/2020.03.21.001206>.
	"""
	
	homepage = "https://github.com/DarkEyes/ipADMIXTURE"
	cran = "ipADMIXTURE" 

	version("0.1.0", md5="59128638b835961ea4208cfc3e0895d5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-treemap", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
