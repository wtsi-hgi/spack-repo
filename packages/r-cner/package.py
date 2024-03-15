# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCner(RPackage):
	"""CNE Detection and Visualization.

	Large-scale identification and advanced visualization of sets of
	conserved noncoding elements."""

	bioc = "CNEr"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CNEr_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CNEr/CNEr_1.38.0.tar.gz"]

	version("1.38.0", md5="56fdc5f3323b1f3efbb8d85584ff75d2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biostrings@2.33.4:", type=("build", "run"))
	depends_on("r-dbi@0.7:", type=("build", "run"))
	depends_on("r-rsqlite@0.11.4:", type=("build", "run"))
	depends_on("r-genomeinfodb@1.1.3:", type=("build", "run"))
	depends_on("r-genomicranges@1.23.16:", type=("build", "run"))
	depends_on("r-rtracklayer@1.25.5:", type=("build", "run"))
	depends_on("r-xvector", type=("build", "run"))
	depends_on("r-genomicalignments@1.1.9:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-readr@0.2.2:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-reshape2@1.4.1:", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))
	depends_on("r-powerlaw@0.60.3:", type=("build", "run"))
	depends_on("r-annotate@1.50:", type=("build", "run"))
	depends_on("r-go-db@3.3:", type=("build", "run"))
	depends_on("r-r-utils@2.3:", type=("build", "run"))
	depends_on("r-keggrest@1.14:", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
