# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgsepd(RPackage):
	"""Gene Set Enrichment / Projection Displays

	R/GSEPD is a bioinformatics package for R to help disambiguate transcriptome samples (a matrix of RNA-Seq counts at transcript IDs) by automating differential expression (with DESeq2), then gene set enrichment (with GOSeq), and finally a N-dimensional projection to quantify in which ways each sample is like either treatment group.
	"""
	
	bioc = "rgsepd" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/rgsepd_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/rgsepd/rgsepd_1.34.0.tar.gz"]

	version("1.34.0", md5="0ca30d2f68c98bcc24cc5c5fbc5951b3")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-goseq@1.28:", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
