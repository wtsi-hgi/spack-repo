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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Rmmquant_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Rmmquant/Rmmquant_1.20.0.tar.gz"]

	version("1.20.0", md5="8f12574d12fdfbb3ef7407666fb22a7b")

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
