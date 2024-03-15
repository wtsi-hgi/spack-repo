# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REbseq(RPackage):
	"""An R package for gene and isoform differential expression analysis of RNA-seq data.

	R/EBSeq is an R package for identifying genes and isoforms differentially
	expressed (DE) across two or more biological conditions in an RNA-seq
	experiment. Details can be found in Leng et al., 2013. It provides the syntax
	required for identifying DE genes and isoforms in a two-group RNA-seq
	experiment as well for identifying DE genes across more than two conditions
	(the commands for identifying DE isoforms across more than two conditions
	are the same as those required for gene-level analysis)."""

	maintainers("pabloaledo")

	bioc = "EBSeq"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/EBSeq_2.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/EBSeq/EBSeq_2.0.0.tar.gz"]

	version("2.0.0", md5="e64aabb38197aba0ee5985a1558cce60")

	depends_on("r-blockmodeling", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
