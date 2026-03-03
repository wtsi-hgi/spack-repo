# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcgh(RPackage):
	"""Comprehensive Pipeline for Analyzing and Visualizing Array-Based CGH Data

	A comprehensive pipeline for analyzing and interactively visualizing genomic profiles generated through commercial or custom aCGH arrays. As inputs, rCGH supports Agilent dual-color Feature Extraction files (.txt), from 44 to 400K, Affymetrix SNP6.0 and cytoScanHD probeset.txt, cychp.txt, and cnchp.txt files exported from ChAS or Affymetrix Power Tools. rCGH also supports custom arrays, provided data complies with the expected format. This package takes over all the steps required for individual genomic profiles analysis, from reading files to profiles segmentation and gene annotations. This package also provides several visualization functions (static or interactive) which facilitate individual profiles interpretation. Input files can be in compressed format, e.g. .bz2 or .gz.
	"""
	
	homepage = "https://github.com/fredcommo/rCGH"
	bioc = "rCGH" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/rCGH_1.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/rCGH/rCGH_1.32.0.tar.gz"]

	version("1.32.0", md5="80510d5207fb0ad5d517a99b35734621")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dnacopy", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-shiny@0.11.1:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-txdb-hsapiens-ucsc-hg18-knowngene", type=("build", "run"))
	depends_on("r-txdb-hsapiens-ucsc-hg19-knowngene", type=("build", "run"))
	depends_on("r-txdb-hsapiens-ucsc-hg38-knowngene", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-acgh", type=("build", "run"))
