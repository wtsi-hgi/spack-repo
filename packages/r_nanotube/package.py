# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNanotube(RPackage):
	"""An Easy Pipeline for NanoString nCounter Data Analysis

	NanoTube includes functions for the processing, quality control, analysis, and visualization of NanoString nCounter data. Analysis functions include differential analysis and gene set analysis methods, as well as postprocessing steps to help understand the results. Additional functions are included to enable interoperability with other Bioconductor NanoString data analysis packages.
	"""
	
	bioc = "NanoTube" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/NanoTube_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/NanoTube/NanoTube_1.8.0.tar.gz"]

	version("1.8.0", md5="524cdc55bcaf670d538be8f6c2f06c11")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-fgsea", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
