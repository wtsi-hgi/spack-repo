# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMfBeta4(RPackage):
	"""Measuring Ecosystem Multi-Functionality and Its Decomposition

	Provide simple functions to (i) compute a class of 
  multi-functionality measures for a single ecosystem for given 
  function weights, (ii) decompose gamma multi-functionality 
  for multiple ecosystems into a within-ecosystem component 
  (alpha multi-functionality) and an among-ecosystem component 
  (beta multi-functionality). In each case, the correlation 
  between functions can be corrected for. Based on biodiversity 
  and ecosystem function data, this software also facilitates 
  graphics for assessing biodiversity-ecosystem functioning 
  relationships across scales. 
	"""
	
	homepage = "https://github.com/AnneChao/MF.beta4"
	cran = "MF.beta4" 

	version("1.0.2", md5="536da141991c31e97493e595a6732290", url="https://cran.r-project.org/src/contrib/MF.beta4_1.0.2.tar.gz")
	version("1.0.1", md5="ad55fd896518a07857d3ea3053aa5cbc", url="https://cran.r-project.org/src/contrib/MF.beta4_1.0.1.tar.gz")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
