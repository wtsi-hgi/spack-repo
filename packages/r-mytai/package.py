# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMytai(RPackage):
	"""Evolutionary Transcriptomics

	Investigate the evolution of biological processes by capturing evolutionary signatures in transcriptomes (Drost et al. (2017) <doi:10.1093/bioinformatics/btx835>). The aim of this tool is to provide a transcriptome analysis environment to quantify the average evolutionary age of genes contributing to a transcriptome of interest (Drost et al. (2016) <doi:10.1101/051565>).
	"""
	
	homepage = "https://github.com/drostlab/myTAI"
	cran = "myTAI" 

	version("0.9.3", md5="d5fad729e270011c6a90619506cde4c8")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-nortest@1.0.2:", type=("build", "run"))
	depends_on("r-fitdistrplus@1.0.2:", type=("build", "run"))
	depends_on("r-foreach@1.4.2:", type=("build", "run"))
	depends_on("r-doparallel@1.0.8:", type=("build", "run"))
	depends_on("r-dplyr@0.3:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-taxize@0.6:", type=("build", "run"))
	depends_on("r-reshape2@1.4.1:", type=("build", "run"))
	depends_on("r-ggplot2@1.0.1:", type=("build", "run"))
	depends_on("r-readr@0.2.2:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
