# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMiscmetabar(RPackage):
	"""Miscellaneous Functions for Metabarcoding Analysis

	Facilitate the description, transformation, exploration, and reproducibility of metabarcoding analyses. 'MiscMetabar' is mainly built on top of the 'phyloseq', 'dada2' and 'targets' R packages. It helps to build reproducible and robust bioinformatics pipelines in R. 'MiscMetabar' makes ecological analysis of alpha and beta-diversity easier, more reproducible and more powerful by integrating a large number of tools. Important features are described in Taudière A. (2023) <doi:10.21105/joss.06038>.
	"""
	
	homepage = "https://github.com/adrientaudiere/MiscMetabar"
	cran = "MiscMetabar" 

	version("0.7.9", md5="787a7d56567774674d43d8d3e1744f6d")
	version("0.7.10", md5="c9bd2dac128ffc5e7d61af919b4bcc65")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-phyloseq", type=("build", "run"))
	depends_on("r-ggplot2@3.5:", type=("build", "run"))
	depends_on("r-dada2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
