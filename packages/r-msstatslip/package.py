# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsstatslip(RPackage):
	"""LiP Significance Analysis in shotgun mass spectrometry-based proteomic experiments

	Tools for LiP peptide and protein significance analysis. Provides functions for summarization, estimation of LiP peptide abundance, and detection of changes across conditions. Utilizes functionality across the MSstats family of packages.
	"""
	
	bioc = "MSstatsLiP"

	version("1.14.1", commit="0915f7892d1a86c867d183a8e3d098952c7b94c5")
	version("1.8.1", md5="677e775b1c84f40715703064cd74faff")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-msstats", type=("build", "run"))
	depends_on("r-msstatsconvert", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-msstatsptm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-factoextra", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
