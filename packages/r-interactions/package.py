# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInteractions(RPackage):
	"""Comprehensive, User-Friendly Toolkit for Probing Interactions

	A suite of functions for conducting and interpreting analysis 
  of statistical interaction in regression models that was formerly part of the 
  'jtools' package. Functionality includes visualization of two- and three-way
  interactions among continuous and/or categorical variables as well as 
  calculation of "simple slopes" and Johnson-Neyman intervals (see e.g., 
  Bauer & Curran, 2005 <doi:10.1207/s15327906mbr4003_5>). These
  capabilities are implemented for generalized linear models in addition to the 
  standard linear regression context.
	"""
	
	homepage = "https://interactions.jacob-long.com"
	cran = "interactions" 

	version("1.1.5", md5="75c6238c25d656f3e544c5a7edd78977")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-jtools@2.0.3:", type=("build", "run"))
	depends_on("r-rlang@0.3:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
