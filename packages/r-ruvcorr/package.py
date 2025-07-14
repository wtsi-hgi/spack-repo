# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRuvcorr(RPackage):
	"""Removal of unwanted variation for gene-gene correlations and related analysis

	RUVcorr allows to apply global removal of unwanted variation (ridged version of RUV) to real and simulated gene expression data.
	"""
	
	bioc = "RUVcorr"

	version("1.40.0", commit="a8b9e538c16576fb82326a9964ddcc59c9004d70")
	version("1.34.0", commit="15ab0609a5a305edc97b25c040d31985ca75fd24")

	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-snowfall", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-bladderbatch", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
