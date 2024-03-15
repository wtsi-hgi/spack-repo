# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCatalyst(RPackage):
	"""Cytometry dATa anALYSis Tools

	CATALYST provides tools for preprocessing of and differential discovery in cytometry data such as FACS, CyTOF, and IMC. Preprocessing includes i) normalization using bead standards, ii) single-cell deconvolution, and iii) bead-based compensation. For differential discovery, the package provides a number of convenient functions for data processing (e.g., clustering, dimension reduction), as well as a suite of visualizations for exploratory data analysis and exploration of results from differential abundance (DA) and state (DS) analysis in order to identify differences in composition and expression profiles at the subpopulation-level, respectively.
	"""
	
	homepage = "https://github.com/HelenaLC/CATALYST"
	bioc = "CATALYST" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CATALYST_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CATALYST/CATALYST_1.26.0.tar.gz"]

	version("1.26.0", md5="6ce647576b86ebdf9fe0933fd87b79ce")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-consensusclusterplus", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-drc", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-flowsom", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-nnls", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-scater", type=("build", "run"))
