# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultileveltools(RPackage):
	"""Multilevel and Mixed Effects Model Diagnostics and Effect Sizes

	Effect sizes, diagnostics and performance metrics for
  multilevel and mixed effects models.
  Includes marginal and conditional 'R2' estimates for linear mixed effects models
  based on Johnson (2014) <doi:10.1111/2041-210X.12225>.
	"""
	
	homepage = "http://joshuawiley.com/multilevelTools"
	cran = "multilevelTools" 

	version("0.1.1", md5="74ce25843e85809492d3cbe7b79921ea")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-data-table@1.12:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-extraoperators@0.1.1:", type=("build", "run"))
	depends_on("r-jwileymisc@1.1:", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
