# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaendtoend(RPackage):
	"""An end to end workflow for differential gene expression using Affymetrix microarrays

	In this article, we walk through an end-to-end Affymetrix microarray differential expression workflow using Bioconductor packages. This workflow is directly applicable to current "Gene" type arrays, e.g. the HuGene or MoGene arrays, but can easily be adapted to similar platforms. The data analyzed here is a typical clinical microarray data set that compares inflamed and non-inflamed colon tissue in two disease subtypes. For each disease, the differential gene expression between inflamed- and non-inflamed colon tissue was analyzed. We will start from the raw data CEL files, show how to import them into a Bioconductor ExpressionSet, perform quality control and normalization and finally differential gene expression (DE) analysis, followed by some enrichment analysis.
	"""
	
	homepage = "https://www.bioconductor.org/help/workflows/"
	bioc = "maEndToEnd" 
	urls = ["https://www.bioconductor.org/packages/3.18/workflows/src/contrib/maEndToEnd_2.22.1.tar.gz", "https://www.bioconductor.org/packages/3.18/workflows/src/contrib/Archive/maEndToEnd/maEndToEnd_2.22.1.tar.gz"]

	version("2.22.1", sha256="48e406d4d5e14e69395e0d6869ed2757c124b3c305405130b42527b832a67bd4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-oligoclasses", type=("build", "run"))
	depends_on("r-arrayexpress", type=("build", "run"))
	depends_on("r-pd-hugene-1-0-st-v1", type=("build", "run"))
	depends_on("r-hugene10sttranscriptcluster-db", type=("build", "run"))
	depends_on("r-oligo", type=("build", "run"))
	depends_on("r-arrayqualitymetrics", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-topgo", type=("build", "run"))
	depends_on("r-reactomepa", type=("build", "run"))
	depends_on("r-clusterprofiler", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-geneplotter", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("r-enrichplot", type=("build", "run"))

