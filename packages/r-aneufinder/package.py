# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAneufinder(RPackage):
	"""Analysis of Copy Number Variation in Single-Cell-Sequencing Data.

	AneuFinder implements functions for copy-number detection, breakpoint
	detection, and karyotype and heterogeneity analysis in single-cell whole
	genome sequencing and strand-seq data."""

	bioc = "AneuFinder"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/AneuFinder_1.30.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/AneuFinder/AneuFinder_1.30.0.tar.gz"]

	version("1.30.0", md5="421efa90a617606c8db2c947d302c6b1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-aneufinderdata", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-biocgenerics@0.31.6:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-bamsignals", type=("build", "run"))
	depends_on("r-dnacopy", type=("build", "run"))
	depends_on("r-ecp", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggdendro", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
