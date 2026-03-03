# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDoser(RPackage):
	"""doseR

	doseR package is a next generation sequencing package for sex chromosome dosage compensation which can be applied broadly to detect shifts in gene expression among an arbitrary number of pre-defined groups of loci. doseR is a differential gene expression package for count data, that detects directional shifts in expression for multiple, specific subsets of genes, broad utility in systems biology research. doseR has been prepared to manage the nature of the data and the desired set of inferences. doseR uses S4 classes to store count data from sequencing experiment. It contains functions to normalize and filter count data, as well as to plot and calculate statistics of count data. It contains a framework for linear modeling of count data. The package has been tested using real and simulated data.
	"""
	
	bioc = "doseR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/doseR_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/doseR/doseR_1.18.0.tar.gz"]

	version("1.18.0", md5="20251942acb7343859507c138bc2b902")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-runit", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
