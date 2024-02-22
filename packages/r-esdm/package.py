# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REsdm(RPackage):
	"""Ensemble Tool for Predictions from Species Distribution Models

	A tool which allows users to create and evaluate ensembles 
    of species distribution model (SDM) predictions. 
    Functionality is offered through R functions or a GUI (R Shiny app). 
    This tool can assist users in identifying spatial uncertainties and 
    making informed conservation and management decisions. The package is 
    further described in Woodman et al (2019) <doi:10.1111/2041-210X.13283>.
	"""
	
	homepage = "https://github.com/smwoodman/eSDM/"
	cran = "eSDM" 

	version("0.4.1", md5="aa1735287ecc19fecf4e1d8140e3ea13")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr@0.7.0:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-sf@0.9.0:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
