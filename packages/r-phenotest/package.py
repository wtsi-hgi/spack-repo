# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhenotest(RPackage):
	"""Tools to test association between gene expression and phenotype in a way that is efficient, structured, fast and scalable. We also provide tools to do GSEA (Gene set enrichment analysis) and copy number variation.

	Tools to test correlation between gene expression and phenotype in a way that is efficient, structured, fast and scalable. GSEA is also provided.
	"""
	
	bioc = "phenoTest" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/phenoTest_1.50.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/phenoTest/phenoTest_1.50.0.tar.gz"]

	version("1.56.0", tag="RELEASE_3_21")
	version("1.50.0", sha256="058e8c210a1dd8f218895a358a5157e4c34bae2d1c916418675a1766955c3543")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
	depends_on("r-heatplus", type=("build", "run"))
	depends_on("r-bma", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-category", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-hopach", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-hgu133a-db", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
