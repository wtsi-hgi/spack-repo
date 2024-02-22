# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicrobiome(RPackage):
	"""Microbiome Analytics

	Utilities for microbiome analysis.
	"""
	
	homepage = "http://microbiome.github.io/microbiome"
	bioc = "microbiome" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/microbiome_1.24.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/microbiome/microbiome_1.24.0.tar.gz"]

	version("1.24.0", md5="2d185cf8b8bf7d23f295dee1af621a0f")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-phyloseq", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-compositions", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
