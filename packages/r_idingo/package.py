# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdingo(RPackage):
	"""Integrative Differential Network Analysis in Genomics

	Fits covariate dependent partial correlation matrices for integrative models to identify differential networks between two groups. The methods are described in Class et. al., (2018) <doi:10.1093/bioinformatics/btx750> and Ha et. al., (2015) <doi:10.1093/bioinformatics/btv406>.
	"""
	
	cran = "iDINGO" 

	version("1.0.4", md5="0ac2a39a387c5983635c4148e1f7ec4b")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-glasso", type=("build", "run"))
	depends_on("r-ggmridge", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
