# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSinglecasees(RPackage):
	"""A Calculator for Single-Case Effect Sizes

	
  Provides R functions for calculating basic effect size indices for 
  single-case designs, including several non-overlap measures and parametric 
  effect size measures, and for estimating the gradual effects model developed 
  by Swan and Pustejovsky (2018) <DOI:10.1080/00273171.2018.1466681>. 
  Standard errors and confidence intervals (based on the assumption that the outcome 
  measurements are mutually independent) are provided for the subset of effect sizes 
  indices with known sampling distributions.
	"""
	
	homepage = "https://jepusto.github.io/SingleCaseES/"
	cran = "SingleCaseES" 

	version("0.7.2", md5="a675546f84364ccc4bd050ce9186ac65")

	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
