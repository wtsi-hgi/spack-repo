# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQripkg(RPackage):
	"""Quantile Regression Index Score

	The QRI_func() function performs quantile regression analysis using age and sex as predictors to calculate the Quantile Regression Index (QRI) score for each individual’s regional brain imaging metrics and then averages across the regional scores to generate an average tissue specific score for each subject. The QRI_plot() is used to plot QRI and generate the normative curves for individual measurements.
	"""
	
	cran = "QRIpkg" 

	version("0.2.2", md5="0b09e4af8017146a11c7abf421051083")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
