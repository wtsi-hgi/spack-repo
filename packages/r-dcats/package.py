# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDcats(RPackage):
	"""Differential Composition Analysis Transformed by a Similarity matrix

	Methods to detect the differential composition abundances between conditions in singel-cell RNA-seq experiments, with or without replicates. It aims to correct bias introduced by missclaisification and enable controlling of confounding covariates. To avoid the influence of proportion change from big cell types, DCATS can use either total cell number or specific reference group as normalization term.
	"""
	
	bioc = "DCATS"

	version("1.6.0", commit="297c738449d0e393c3265920d1358c883e69839b")
	version("1.0.0", commit="70f83be6ac82b72972c722eefa6604d0464ef9de")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-aod", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
