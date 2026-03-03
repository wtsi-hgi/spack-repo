# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSysrecon(RPackage):
	"""Systematical Metabolic Reconstruction

	In the past decade, genome-scale metabolic reconstructions have widely been 
    used to comprehend the systems biology of metabolic pathways within an organism. 
    Different GSMs are constructed using various techniques that 
    require distinct steps, but the input data, information conversion and software tools
    are neither concisely defined nor mathematically or programmatically formulated
    in a context-specific manner.The tool that quantitatively and qualitatively specifies
    each reconstruction steps and can generate a template list of reconstruction steps dynamically
    selected from a reconstruction step reservoir, constructed based on all available published papers.
	"""
	
	homepage = "https://oyshilin.github.io/sysrecon/"
	cran = "Sysrecon" 

	version("0.1.3", md5="831584dc91715c2df1846b64dba1a48f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggtree", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-snowballc", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
