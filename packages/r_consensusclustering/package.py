# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConsensusclustering(RPackage):
	"""Consensus Clustering

	Clustering, or cluster analysis, is a widely used technique in bioinformatics to identify groups of similar biological data points. Consensus clustering is an extension to clustering algorithms that aims to construct a robust result from those clustering features that are invariant under different sources of variation. For the reference, please cite the following paper: Yousefi, Melograna, et. al., (2023) <doi:10.3389/fmicb.2023.1170391>.
	"""
	
	cran = "ConsensusClustering" 

	version("1.2.0", md5="a8eccc46958fda179eedcd40a2b70bf0")

	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
