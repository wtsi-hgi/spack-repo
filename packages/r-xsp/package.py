# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXsp(RPackage):
	"""The Chi-Square Periodogram

	The circadian period of a time series data is predicted and the statistical significance of the periodicity are calculated using the chi-square periodogram.
	"""
	
	cran = "xsp" 

	version("0.1.2", md5="b5f7e3438143592afd6c8f75dd698942")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
