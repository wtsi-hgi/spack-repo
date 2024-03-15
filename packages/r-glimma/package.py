# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlimma(RPackage):
	"""Interactive HTML graphics.

	This package generates interactive visualisations for analysis of RNA-
	sequencing data using output from limma, edgeR or DESeq2 packages in an
	HTML page. The interactions are built on top of the popular static
	representations of analysis results in order to provide additional
	information."""

	bioc = "Glimma"

	license("LGPL-3.0-only")
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Glimma_2.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Glimma/Glimma_2.12.0.tar.gz"]

	version("2.12.0", md5="bea9aeee00dca519586661d33ba8dc74")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
