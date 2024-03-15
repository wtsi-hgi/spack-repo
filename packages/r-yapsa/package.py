# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYapsa(RPackage):
	"""Yet Another Package for Signature Analysis.

	This package provides functions and routines useful in the analysis of
	somatic signatures (cf. L. Alexandrov et al., Nature 2013). In
	particular, functions to perform a signature analysis with known
	signatures (LCD = linear combination decomposition) and a signature
	analysis on stratified mutational catalogue (SMC = stratify mutational
	catalogue) are provided."""

	bioc = "YAPSA"

	license("GPL-3.0-or-later")
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/YAPSA_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/YAPSA/YAPSA_1.28.0.tar.gz"]

	version("1.28.0", md5="7da75a0c0eabc79012aeb87c9a6e9582")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-limsolve", type=("build", "run"))
	depends_on("r-somaticsignatures", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-getoptlong", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-gtrellis", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-pmcmrplus", type=("build", "run"))
	depends_on("r-ggbeeswarm", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-keggrest", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-bsgenome-hsapiens-ucsc-hg19", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
