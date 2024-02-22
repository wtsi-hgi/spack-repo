# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtsplot(RPackage):
	"""Time Series Plot

	A fast and elegant time series visualization package. In addition to the 
	standard R plot types, this package supports candle sticks, open-high-low-close, and
	volume plots. Useful for visualizing any time series data, e.g., stock prices and 
	technical indicators.
	"""
	
	homepage = "https://bitbucket.org/rtsvizteam/rtsplot"
	cran = "rtsplot" 

	version("0.1.5", md5="ffff76e68aedb874bd6595a0ec64bfc7")

	depends_on("r-xts", type=("build", "run"))
	depends_on("r-quantmod", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
