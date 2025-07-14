# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsca(RPackage):
	"""GSCA: Gene Set Context Analysis

	GSCA takes as input several lists of activated and repressed genes. GSCA then searches through a compendium of publicly available gene expression profiles for biological contexts that are enriched with a specified pattern of gene expression. GSCA provides both traditional R functions and interactive, user-friendly user interface.
	"""
	
	bioc = "GSCA" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GSCA_2.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GSCA/GSCA_2.32.0.tar.gz"]

    version("2.38.0", tag="RELEASE_3_21")
	version("2.32.0", sha256="4bf850c901a8a519cf45143e7d1236d0359310cf5eaad460cfd829f933c91f19")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
