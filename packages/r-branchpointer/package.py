# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBranchpointer(RPackage):
	"""Prediction of intronic splicing branchpoints

	Predicts branchpoint probability for sites in intronic branchpoint windows. Queries can be supplied as intronic regions; or to evaluate the effects of mutations, SNPs.
	"""
	
	bioc = "branchpointer" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/branchpointer_1.28.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/branchpointer/branchpointer_1.28.0.tar.gz"]

	version("1.28.0", md5="7a62abd020843736b7ea125ffc4a56e0")

	depends_on("r-caret", type=("build", "run"))
	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-bsgenome-hsapiens-ucsc-hg38", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
