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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/microbiome_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/microbiome/microbiome_1.24.0.tar.gz"]

	version("1.30.0", tag="RELEASE_3_21")
	version("1.24.0", sha256="05b8dc9433b64cf7dfec1eb8b35352df58bde841bbe39fe5a5dc26b48fe3b376")

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
