# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMumosa(RPackage):
	"""Multi-Modal Single-Cell Analysis Methods

	Assorted utilities for multi-modal analyses of single-cell datasets. Includes functions to combine multiple modalities for downstream analysis, perform MNN-based batch correction across multiple modalities, and to compute correlations between assay values for different modalities.
	"""
	
	homepage = "http://bioconductor.org/packages/mumosa"
	bioc = "mumosa"

	version("1.16.0", commit="31f2c64fc9d2b16952d2cede8742a01a968137d8")
	version("1.10.0", commit="f52c95ab75ac0af2b52f6cf9ea38928e727e48e6")

	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-delayedmatrixstats", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biocneighbors", type=("build", "run"))
	depends_on("r-biocsingular", type=("build", "run"))
	depends_on("r-scaledmatrix", type=("build", "run"))
	depends_on("r-beachmat", type=("build", "run"))
	depends_on("r-scuttle", type=("build", "run"))
	depends_on("r-metapod", type=("build", "run"))
	depends_on("r-scran", type=("build", "run"))
	depends_on("r-batchelor", type=("build", "run"))
	depends_on("r-uwot", type=("build", "run"))
