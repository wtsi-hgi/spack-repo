# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMethylationarrayanalysis(RPackage):
	"""A cross-package Bioconductor workflow for analysing methylation array data.

	Methylation in the human genome is known to be associated with development and disease. The Illumina Infinium methylation arrays are by far the most common way to interrogate methylation across the human genome. This Bioconductor workflow uses multiple packages for the analysis of methylation array data. Specifically, we demonstrate the steps involved in a typical differential methylation analysis pipeline including: quality control, filtering, normalization, data exploration and statistical testing for probe-wise differential methylation. We further outline other analyses such as differential methylation of regions, differential variability analysis, estimating cell type composition and gene ontology testing. Finally, we provide some examples of how to visualise methylation array data.
	"""
	
	bioc = "methylationArrayAnalysis"

	version("1.32.0", commit="793d64214c64d09410703cf8acc3ac79e89270f9")
	version("1.26.0", commit="60b2530a2be8efc171297df8cd15a5006132ae6c")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-biocstyle", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-minfi", type=("build", "run"))
	depends_on("r-illuminahumanmethylation450kanno-ilmn12-hg19", type=("build", "run"))
	depends_on("r-illuminahumanmethylation450kmanifest", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-missmethyl", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-minfidata", type=("build", "run"))
	depends_on("r-gviz", type=("build", "run"))
	depends_on("r-dmrcate", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-flowsorted-blood-450k", type=("build", "run"))

