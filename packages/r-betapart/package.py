# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBetapart(RPackage):
	"""Partitioning Beta Diversity into Turnover and Nestedness
Components

	Functions to compute pair-wise dissimilarities (distance matrices) and multiple-site dissimilarities, separating the turnover and nestedness-resultant components of taxonomic (incidence and abundance based), functional and phylogenetic beta diversity.
	"""
	
	cran = "betapart" 

	version("1.6", md5="daabc42a7234054a75e9354863406fbe")

	depends_on("r-ape", type=("build", "run"))
	depends_on("r-fastmatch", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-picante", type=("build", "run"))
	depends_on("r-rcdd", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-snow", type=("build", "run"))
	depends_on("r-itertools", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
