# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFgsea(RPackage):
	"""Fast Gene Set Enrichment Analysis.

	The package implements an algorithm for fast gene set enrichment
	analysis. Using the fast algorithm allows to make more permutations and
	get more fine grained p-values, which allows to use accurate stantard
	approaches to multiple hypothesis correction."""

	bioc = "fgsea"

	license("MIT")
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/fgsea_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/fgsea/fgsea_1.28.0.tar.gz"]

	version("1.28.0", md5="53b8ab8a13390a0920bc13eeba3aa1b8")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-fastmatch", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
