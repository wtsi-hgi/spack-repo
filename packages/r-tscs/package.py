# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTscs(RPackage):
	"""Time Series Cointegrated System

	A set of functions to implement Time Series Cointegrated System (TSCS)
    spatial interpolation and relevant data visualization.
	"""
	
	cran = "TSCS" 

	version("0.1.1", md5="4926b791a71c574ab04645127deae32c")

	depends_on("r@3.4.2:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-tseries@0.10.42:", type=("build", "run"))
	depends_on("r-rgl@0.98.1:", type=("build", "run"))
