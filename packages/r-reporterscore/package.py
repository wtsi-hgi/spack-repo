# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReporterscore(RPackage):
	"""Generalized Reporter Score-Based Enrichment Analysis for Omics
Data

	Inspired by the classic 'RSA', we developed the improved 'Generalized Reporter 
    Score-based Analysis (GRSA)' method, implemented in the R package 'ReporterScore', along 
    with comprehensive visualization methods and pathway databases. 'GRSA' is a threshold-free 
    method that works well with all types of biomedical features, such as genes, chemical compounds, 
    and microbial species. Importantly, the 'GRSA' supports multi-group and longitudinal experimental 
    designs, because of the included multi-group-compatible statistical methods. 
	"""
	
	homepage = "https://github.com/Asa12138/ReporterScore"
	cran = "ReporterScore" 

	version("0.1.2", md5="3bebfa19d6e47b824624a49ca925424a")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2@3.2:", type=("build", "run"))
	depends_on("r-pcutils", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ggnewscale", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
