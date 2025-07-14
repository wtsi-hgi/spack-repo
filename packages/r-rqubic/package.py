# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRqubic(RPackage):
	"""Qualitative biclustering algorithm for expression data analysis in R

	This package implements the QUBIC algorithm introduced by Li et al. for the qualitative biclustering with gene expression data.
	"""
	
	bioc = "rqubic"

	version("1.54.0", commit="fa5ffea568acd2ced8e0cd2afcf3fd7860f9ac91")
	version("1.48.0", commit="2f412019ed39216bd1f03cba091518dabffb0952")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biclust", type=("build", "run"))
