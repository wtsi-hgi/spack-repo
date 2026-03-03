# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCopsens(RPackage):
	"""Copula-Based Sensitivity Analysis for Observational Causal
Inference

	Implements the copula-based sensitivity analysis method, 
  as discussed in Copula-based Sensitivity Analysis for Multi-Treatment Causal Inference with Unobserved Confounding
  <arXiv:2102.09412>, with Gaussian copula adopted in particular.
	"""
	
	homepage = "https://github.com/JiajingZ/CopSens"
	cran = "CopSens" 

	version("0.1.0", md5="429faefb1b86ba8910e8da4c70142015")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-pcamethods@1.78:", type=("build", "run"))
	depends_on("r-cvxr@1:", type=("build", "run"))
	depends_on("r-mass@7.3.53:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.3:", type=("build", "run"))
	depends_on("r-dplyr@1.0.3:", type=("build", "run"))
	depends_on("r-tidyr@1.1.2:", type=("build", "run"))
	depends_on("r-tidyverse@1.3:", type=("build", "run"))
