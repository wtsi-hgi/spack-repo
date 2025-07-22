# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RToast(RPackage):
	"""Tools for the analysis of heterogeneous tissues

	This package is devoted to analyzing high-throughput data (e.g. gene expression microarray, DNA methylation microarray, RNA-seq) from complex tissues. Current functionalities include 1. detect cell-type specific or cross-cell type differential signals 2. tree-based differential analysis 3. improve variable selection in reference-free deconvolution 4. partial reference-free deconvolution with prior knowledge.
	"""
	
	bioc = "TOAST"

	version("1.22.0", commit="d37b279d7a29eba9ee0e2e4d2fe84fb2fa5fbfd2")
	version("1.16.0", commit="404044b976b2bc4c9ff05b4249f4fce3720528dd")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-epidish", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-nnls", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
