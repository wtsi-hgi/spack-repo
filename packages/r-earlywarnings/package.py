# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REarlywarnings(RPackage):
	"""Early Warning Signals for Critical Transitions in Time Series

	The Early-Warning-Signals Toolbox provides methods for estimating
    statistical changes in time series that can be used for identifying nearby
    critical transitions. 
	"""
	
	homepage = "http://www.early-warning-signals.org"
	cran = "earlywarnings" 

	version("1.1.29", md5="b8f7d8c8fc0a39cc0b73ac0cd077c373")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-tgp", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-nortest", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-kendall", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-som", type=("build", "run"))
	depends_on("r-spam", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
