# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgbio(RPackage):
	"""Visualization tools for genomic data.

	The ggbio package extends and specializes the grammar of graphics for
	biological data. The graphics are designed to answer common scientific
	questions, in particular those often asked of high throughput genomics
	data. All core Bioconductor data structures are supported, where
	appropriate. The package supports detailed views of particular genomic
	regions, as well as genome-wide overviews. Supported overviews include
	ideograms and grand linear views. High-level plots include sequence
	fragment length, edge-linked interval to data view, mismatch pileup, and
	several splicing summaries."""

	bioc = "ggbio"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ggbio_1.50.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ggbio/ggbio_1.50.0.tar.gz"]

	version("1.50.0", md5="de7ec73480f41c35fca2a8a758fbc7d0")

	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-ggplot2@1:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-biovizbase@1.29.2:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-s4vectors@0.13.13:", type=("build", "run"))
	depends_on("r-iranges@2.11.16:", type=("build", "run"))
	depends_on("r-genomeinfodb@1.1.3:", type=("build", "run"))
	depends_on("r-genomicranges@1.29.14:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-rsamtools@1.17.28:", type=("build", "run"))
	depends_on("r-genomicalignments@1.1.16:", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-variantannotation@1.11.4:", type=("build", "run"))
	depends_on("r-rtracklayer@1.25.16:", type=("build", "run"))
	depends_on("r-genomicfeatures@1.29.11:", type=("build", "run"))
	depends_on("r-organismdbi", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-ensembldb@1.99.13:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-annotationfilter", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
