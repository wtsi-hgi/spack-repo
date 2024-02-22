# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPredtools(RPackage):
	"""Prediction Model Tools

	Provides additional functions for evaluating predictive models, including plotting calibration curves and model-based Receiver Operating Characteristic (mROC) based on Sadatsafavi et al (2021) <arXiv:2003.00316>. 
	"""
	
	homepage = "https://github.com/resplab/predtools"
	cran = "predtools" 

	version("0.0.3", md5="9626eb528b742524222eade9784d97e2")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-rconics", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
