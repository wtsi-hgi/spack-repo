# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REbseq(RPackage):
	"""An R package for gene and isoform differential expression analysis of RNA-seq data

	Differential Expression analysis at both gene and isoform level using RNA-seq data
	"""
	
	bioc = "EBSeq" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/EBSeq_2.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/EBSeq/EBSeq_2.0.0.tar.gz"]

    version("2.6.0", tag="RELEASE_3_21")
	version("2.0.0", sha256="9c5818ed988a1b3e416f3300ad56d4ae778485deb3b51eb6ee31bea91074a91f")

	depends_on("r-blockmodeling", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
