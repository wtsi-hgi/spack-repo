# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMusica(RPackage):
	"""Multiscale Climate Model Assessment

	Provides functions allowing for (1) easy aggregation of multivariate time series into custom time scales, (2) comparison of statistical summaries between different data sets at multiple time scales (e.g. observed and bias-corrected data), (3) comparison of relations between variables and/or different data sets at multiple time scales (e.g. correlation of precipitation and temperature in control and scenario simulation) and (4) transformation of time series at custom time scales.
	"""
	
	cran = "musica" 

	version("0.1.3", md5="9afa07c9bbfa948d6ef05acfb1f66b1f")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-qmap", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
