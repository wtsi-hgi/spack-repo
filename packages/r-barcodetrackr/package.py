# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBarcodetrackr(RPackage):
	"""Functions for Analyzing Cellular Barcoding Data

	barcodetrackR is an R package developed for the analysis and visualization of clonal tracking data. Data required is samples and tag abundances in matrix form. Usually from cellular barcoding experiments, integration site retrieval analyses, or similar technologies.
	"""
	
	homepage = "https://github.com/dunbarlabNIH/barcodetrackR"
	bioc = "barcodetrackR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/barcodetrackR_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/barcodetrackR/barcodetrackR_1.10.0.tar.gz"]

	version("1.10.0", sha256="096ac951ed4c2259c9bdd60e9d7308955b88418dad6b5cfd116fb8a77033b7f0")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggdendro", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
