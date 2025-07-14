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

	version("2.38.0", commit="5bfe21ec58492f3e6b090b8506d31ffa28e7c518")
	version("2.32.0", commit="b2337bea1956778a5f83805628afed90352e395d")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
