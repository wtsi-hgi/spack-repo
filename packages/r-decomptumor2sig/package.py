# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDecomptumor2sig(RPackage):
	"""Decomposition of individual tumors into mutational signatures by signature refitting

	Uses quadratic programming for signature refitting, i.e., to decompose the mutation catalog from an individual tumor sample into a set of given mutational signatures (either Alexandrov-model signatures or Shiraishi-model signatures), computing weights that reflect the contributions of the signatures to the mutation load of the tumor.
	"""
	
	homepage = "http://rmpiro.net/decompTumor2Sig/"
	bioc = "decompTumor2Sig"

	version("2.24.0", commit="c68d8e237691a3fd2545f09e4fe6b782945a8cb6")
	version("2.18.0", commit="d01f0b59965a447457efd9c99c908f9710dc4464")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-quadprog@1.5.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-bsgenome-hsapiens-ucsc-hg19", type=("build", "run"))
	depends_on("r-txdb-hsapiens-ucsc-hg19-knowngene", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-ggseqlogo", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-ggseqlogo", type=("build", "link", "run"))
