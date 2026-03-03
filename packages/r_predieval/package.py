# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPredieval(RPackage):
	"""Assessing Performance of Prediction Models for Predicting
Patient-Level Treatment Benefit

	Methods for assessing the performance of a prediction model with respect to identifying patient-level treatment benefit. All methods are applicable for continuous and binary outcomes, and for any type of statistical or machine-learning prediction model as long as it uses baseline covariates to predict outcomes under treatment and control. 
	"""
	
	homepage = "https://github.com/esm-ispm-unibe-ch/predieval"
	cran = "predieval" 

	version("0.1.1", md5="9c83d6e66820dcde19bead0d465db2eb")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-hmisc@4.6.0:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-mass@7.3:", type=("build", "run"))
	depends_on("r-matching@4.10.2:", type=("build", "run"))
