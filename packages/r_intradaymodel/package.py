# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntradaymodel(RPackage):
	"""Modeling and Forecasting Financial Intraday Signals

	Models, analyzes, and forecasts financial intraday signals. This package
    currently supports a univariate state-space model for intraday trading volume provided
    by Chen (2016) <doi:10.2139/ssrn.3101695>.
	"""
	
	homepage = "https://github.com/convexfi/intradayModel"
	cran = "intradayModel" 

	version("0.0.1", md5="66cdec98bd813d29a3e08db4293e9652")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
