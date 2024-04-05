# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmdiff2(RPackage):
	"""Statistical Testing for ChIP-Seq data sets

	This package detects statistically significant differences between read enrichment profiles in different ChIP-Seq samples. To take advantage of shape differences it uses Kernel methods (Maximum Mean Discrepancy, MMD).
	"""
	
	bioc = "MMDiff2" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MMDiff2_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MMDiff2/MMDiff2_1.30.0.tar.gz"]

	version("1.30.0", md5="6d14e03f2d5842c403a50c41f30c82d1", url="https://www.bioconductor.org/packages/release/bioc/src/contrib/MMDiff2_1.30.0.tar.gz")
	version("1.30.0", md5="6d14e03f2d5842c403a50c41f30c82d1", url="https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MMDiff2_1.30.0.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
