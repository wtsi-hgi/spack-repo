# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExtremeindex(RPackage):
	"""Forecast Verification for Extreme Events

	An index measuring the amount of information brought by forecasts for extreme events, subject to calibration, is computed. This index is originally designed for weather or climate forecasts, but it may be used in other forecasting contexts. This is the implementation of the index in Taillardat et al. (2019) <arXiv:1905.04022>.
	"""
	
	cran = "extremeIndex" 

	version("0.0.3", md5="a14be3304b305c2038ed19383b49e672")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-evd", type=("build", "run"))
	depends_on("r-gmm", type=("build", "run"))
	depends_on("r-evir", type=("build", "run"))
