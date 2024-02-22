# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFtsa(RPackage):
	"""Functional Time Series Analysis

	Functions for visualizing, modeling, forecasting and hypothesis testing of functional time series.
	"""
	
	cran = "ftsa" 

	version("6.4", md5="8218892538195d7f0a6b464e7a676265")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-rainbow", type=("build", "run"))
	depends_on("r-sde", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pcapp", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-pdfcluster", type=("build", "run"))
	depends_on("r-ecp", type=("build", "run"))
	depends_on("r-strucchange", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-fgarch", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-vars", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-fdapace", type=("build", "run"))
	depends_on("r-laplacesdemon", type=("build", "run"))
	depends_on("r-evgam", type=("build", "run"))
	depends_on("r-roopsd", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
