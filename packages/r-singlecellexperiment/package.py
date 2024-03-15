# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SingleCellExperiment_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SingleCellExperiment/SingleCellExperiment_1.24.0.tar.gz"]

	version("1.24.0", md5="ef057b77f40efba992f311486e83448b")

	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
