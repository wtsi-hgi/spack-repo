# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCalibrationband(RPackage):
	"""Calibration Bands

	Package to assess the calibration of probabilistic classifiers using confidence bands for monotonic functions. Besides testing the classical goodness-of-fit null hypothesis of perfect calibration, the confidence bands calculated within that package facilitate inverted goodness-of-fit tests whose rejection allows for a sought-after conclusion of a sufficiently well-calibrated model. The package creates flexible graphical tools to perform these tests.  For construction details see also Dimitriadis, Dümbgen, Henzi, Puke, Ziegel (2022) <arXiv:2203.04065>. 
	"""
	
	homepage = "https://github.com/marius-cp/calibrationband"
	cran = "calibrationband" 

	version("0.2.1", md5="3e3a2614c27300649f79836b52a2fe9a")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
