# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROncofilterfast(RPackage):
	"""Aids in the Analysis of Genes Influencing Cancer Survival

	Aids in the analysis of genes influencing cancer survival by including a principal function, calculator(), which calculates the P-value for each provided gene under the optimal cutoff in cancer survival studies. Grounded in methodologies from significant works, this package references Therneau's 'survival' package (Therneau, 2024; <https://CRAN.R-project.org/package=survival>) and the survival analysis extensions by Therneau and Grambsch (2000, ISBN 0-387-98784-3). It also integrates the 'survminer' package by Kassambara et al. (2021; <https://CRAN.R-project.org/package=survminer>), enhancing survival curve visualizations with 'ggplot2'.
	"""
	
	cran = "Oncofilterfast" 

	version("1.0.0", md5="cccd85b6df7faccffbb531937292e81b")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-survminer", type=("build", "run"))
