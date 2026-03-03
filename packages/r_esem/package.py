# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REsem(RPackage):
	"""Exploratory Structural Equation Modeling ESEM

	A collection of functions developed to support the tutorial on using Exploratory Structural Equiation Modeling (ESEM) (Asparouhov & Muthén, 2009) <https://www.statmodel.com/download/EFACFA810.pdf>) with Longitudinal Study of Australian Children (LSAC) dataset (Mohal et al., 2023) <doi:10.26193/QR4L6Q>. 
    The package uses 'tidyverse','psych', 'lavaan','semPlot' and provides additional functions to conduct ESEM. 
    The package provides general functions to complete ESEM, including esem_c(), creation of target matrix (if it is used) make_target(), generation of the Confirmatory Factor Analysis (CFA) model syntax esem_cfa_syntax(). 
    A sample data is provided - the package includes a sample data of the Strengths and Difficulties Questionnaire of the Longitudinal Study of Australian Children (SDQ LSAC) in sdq_lsac().  
    'ESEM' package vignette presents the tutorial demonstrating the use of ESEM on SDQ LSAC data. 
	"""
	
	homepage = "https://github.com/maria-pro/esem"
	cran = "esem" 

	version("2.0.0", md5="3204ccbabfe4254520e6b43aea1d2f8f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-gparotation", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
