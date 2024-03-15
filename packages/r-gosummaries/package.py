# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGosummaries(RPackage):
	"""Word cloud summaries of GO enrichment analysis

	A package to visualise Gene Ontology (GO) enrichment analysis results on gene lists arising from different analyses such clustering or PCA. The significant GO categories are visualised as word clouds that can be combined with different plots summarising the underlying data.
	"""
	
	homepage = "https://github.com/raivokolde/GOsummaries"
	bioc = "GOsummaries" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GOsummaries_2.37.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GOsummaries/GOsummaries_2.37.0.tar.gz"]

	version("2.37.0", md5="e31e67ed4c66122dcf79a694096ef539")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-gprofiler", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
