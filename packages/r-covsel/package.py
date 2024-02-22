# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovsel(RPackage):
	"""Model-Free Covariate Selection

	Model-free selection of covariates under unconfoundedness for situations where the parameter of interest is an average causal effect. This package is based on  model-free backward elimination algorithms proposed in de Luna, Waernbaum and Richardson (2011). Marginal co-ordinate hypothesis testing is used in situations where all covariates are continuous while kernel-based smoothing appropriate for mixed data is used otherwise.
	"""
	
	cran = "CovSel" 

	version("1.2.1", md5="58cc8219ed2fd9b670856936e17136cd")

	depends_on("r-dr", type=("build", "run"))
	depends_on("r-np", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
