# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImpactflu(RPackage):
	"""Quantification of Population-Level Impact of Vaccination

	
  Implements the compartment model from Tokars (2018) 
  <doi:10.1016/j.vaccine.2018.10.026>. This enables quantification of 
  population-wide impact of vaccination against vaccine-preventable 
  diseases such as influenza.
	"""
	
	cran = "impactflu" 

	version("0.1.0", md5="c91439056a1385b2f8d9f9d95cd90170")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
