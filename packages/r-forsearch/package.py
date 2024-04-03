# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForsearch(RPackage):
	"""Diagnostic Analysis Using Forward Search Procedure for Various
Models

	Identifies potential data outliers and their impact on estimates and 
         analyses. Uses the forward search approach of Atkinson and Riani, "Robust 
         Diagnostic Regression Analysis", 2000,<ISBN: o-387-95017-6> to prepare 
         descriptive statistics of a dataset that is to be analyzed by stats::lm(), 
         stats::glm(), stats::nls(), nlme::lme() or survival::coxph().  Includes 
         graphics functions to display the descriptive statistics.
	"""
	
	cran = "forsearch" 

	version("6.0.0", md5="e6dac4a36e48b4ed2ffa5784e0f566a2")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-hmisc@4.7.0:", type=("build", "run"))
	depends_on("r-cairo@1.6.0:", type=("build", "run"))
	depends_on("r-formula-tools@1.7:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-nlme@3.1.157:", type=("build", "run"))
	depends_on("r-survival@3.4:", type=("build", "run"))
	depends_on("r-tibble@3.1.8:", type=("build", "run"))
	depends_on("gmp@4.1:", type=("build", "link", "run"))
