# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnsr(RPackage):
	"""Elastic Net SearcheR

	Elastic net regression models are controlled by two parameters,
  lambda, a measure of shrinkage, and alpha, a metric defining the model's
  location on the spectrum between ridge and lasso regression.  
  glmnet provides tools for selecting lambda via cross
  validation but no automated methods for selection of alpha.  Elastic Net
  SearcheR automates the simultaneous selection of both lambda and alpha.
  Developed, in part, with support by NICHD R03 HD094912.
	"""
	
	homepage = "https://github.com/dewittpe/ensr"
	cran = "ensr" 

	version("0.1.0", md5="2fd55ad8dc174d2bc6d0dae9e786cc24")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
