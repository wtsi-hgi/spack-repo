# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetanet(RPackage):
	"""Network Analysis for Omics Data

	Comprehensive network analysis package.
    Calculate correlation network fastly, accelerate lots of analysis by parallel computing.
    Support for multi-omics data, search sub-nets fluently.
    Handle bigger data, more than 10,000 nodes in each omics.
    Offer various layout method for multi-omics network and some interfaces to other software ('Gephi', 'Cytoscape', 'ggplot2'), easy to visualize.
    Provide comprehensive topology indexes calculation, including ecological network stability.
	"""
	
	homepage = "https://github.com/Asa12138/MetaNet"
	cran = "MetaNet" 

	version("0.1.2", md5="bdb3f67df24842c3d375628911399995")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-igraph@1.3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2@3.2:", type=("build", "run"))
	depends_on("r-ggnewscale", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-pcutils@0.2.5:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
