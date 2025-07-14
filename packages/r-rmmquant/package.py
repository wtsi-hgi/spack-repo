# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmmquant(RPackage):
	"""RNA-Seq multi-mapping Reads Quantification Tool

	RNA-Seq is currently used routinely, and it provides accurate information on gene transcription. However, the method cannot accurately estimate duplicated genes expression. Several strategies have been previously used, but all of them provide biased results. With Rmmquant, if a read maps at different positions, the tool detects that the corresponding genes are duplicated; it merges the genes and creates a merged gene. The counts of ambiguous reads is then based on the input genes and the merged genes. Rmmquant is a drop-in replacement of the widely used tools findOverlaps and featureCounts that handles multi-mapping reads in an unabiased way.
	"""
	
	bioc = "Rmmquant"

	version("1.26.0", commit="7b3d5f846a1d2a3695251562cad5981ec4fd6a24")
	version("1.20.0", commit="89552c3bce1ef822ce28e043628a639ea6b5d3f1")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-tbx20bamsubset", type=("build", "run"))
	depends_on("r-txdb-mmusculus-ucsc-mm9-knowngene", type=("build", "run"))
	depends_on("r-org-mm-eg-db", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-apeglm", type=("build", "run"))
	depends_on("r-biocstyle", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
