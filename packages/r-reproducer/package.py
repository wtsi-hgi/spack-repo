# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReproducer(RPackage):
	"""Reproduce Statistical Analyses and Meta-Analyses

	Includes data analysis and meta-analysis functions (e.g., to 
    calculate effect sizes and 95% Confidence Intervals (CI) on Standardised 
    Effect Sizes (d) for AB/BA cross-over repeated-measures experimental 
    designs), data presentation functions (e.g., density curve overlaid on 
    histogram),and the data sets analyzed in different research papers in 
    software engineering (e.g., related to software defect prediction or multi-
    site experiment concerning the extent to which structured abstracts were
    clearer and more complete than conventional abstracts) to streamline
    reproducible research in software engineering.
	"""
	
	homepage = "https://madeyski.e-informatyka.pl/reproducible-research/"
	cran = "reproducer" 

	version("0.5.3", md5="0f4ee1787cf5e35e8d6a2cb6beaed9fd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@0.8.0.1:", type=("build", "run"))
	depends_on("r-getoptlong@0.1.7:", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-gridextra@0.9.1:", type=("build", "run"))
	depends_on("r-httr@1.4:", type=("build", "run"))
	depends_on("r-jsonlite@1.6:", type=("build", "run"))
	depends_on("r-lme4@1.1.10:", type=("build", "run"))
	depends_on("r-mass@7.3.45:", type=("build", "run"))
	depends_on("r-metafor@1.9.2:", type=("build", "run"))
	depends_on("r-nortest@1.0.4:", type=("build", "run"))
	depends_on("r-openxlsx@2.4:", type=("build", "run"))
	depends_on("r-readr@1.3.1:", type=("build", "run"))
	depends_on("r-reshape@0.8.8:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tibble@2.1.1:", type=("build", "run"))
	depends_on("r-tidyr@0.8.3:", type=("build", "run"))
	depends_on("r-xtable@1.7.4:", type=("build", "run"))
