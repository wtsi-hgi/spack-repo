# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCeda(RPackage):
	"""CRISPR Screen and Gene Expression Differential Analysis

	Provides analytical methods for analyzing CRISPR screen data
    at different levels of gene expression. Multi-component normal mixture models
    and EM algorithms are used for modeling.
	"""
	
	cran = "CEDA" 

	version("1.1.0", md5="d8694e0fc776cb0aae2ac7b10027c53e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-mixtools", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggsci", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-ggprism", type=("build", "run"))
