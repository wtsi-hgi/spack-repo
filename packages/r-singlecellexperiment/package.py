# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSinglecellexperiment(RPackage):
	"""S4 Classes for Single Cell Data.

	Defines a S4 class for storing data from single-cell experiments. This
	includes specialized methods to store and retrieve spike-in information,
	dimensionality reduction coordinates and size factors for each cell,
	along with the usual metadata for genes and libraries."""

	bioc = "SingleCellExperiment"

	version("1.24.0", commit="2fd8e495dabb35e8870d661e7fe6da032f47bc71")

	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
