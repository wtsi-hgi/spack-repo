# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPricesensitivitymeter(RPackage):
	"""Van Westendorp Price Sensitivity Meter Analysis

	An implementation of the van Westendorp Price
    Sensitivity Meter in R, which is a survey-based approach
	to analyze consumer price preferences and sensitivity
    (van Westendorp 1976, isbn:9789283100386).
	"""
	
	homepage = "https://max-alletsee.github.io/pricesensitivitymeter/"
	cran = "pricesensitivitymeter" 

	version("1.2.2", md5="4a836aab2aec5c0a976eee99bbf2942b")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-survey@3.23.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
