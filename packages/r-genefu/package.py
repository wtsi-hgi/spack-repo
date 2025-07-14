# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenefu(RPackage):
	"""Computation of Gene Expression-Based Signatures in Breast Cancer

	This package contains functions implementing various tasks usually required by gene expression analysis, especially in breast cancer studies: gene mapping between different microarray platforms, identification of molecular subtypes, implementation of published gene signatures, gene selection, and survival analysis.
	"""
	
	homepage = "http://www.pmgenomics.ca/bhklab/software/genefu"
	bioc = "genefu"

	version("2.40.0", commit="2523636d3a19ebb10300e4e7185364d5a359dd4c")
	version("2.34.0", commit="6911d3c6fc20fbe15374a977b393c839d179b709")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-survcomp", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-ic10", type=("build", "run"))
	depends_on("r-aims", type=("build", "run"))
	depends_on("r-amap", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
