# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBreakpoint(RPackage):
	"""An R Package for Multiple Break-Point Detection via the
Cross-Entropy Method

	Implements the Cross-Entropy (CE) method, which is a model based stochastic optimization technique to estimate both the number and their corresponding locations of break-points in continuous and discrete measurements (Priyadarshana and Sofronov (2015), Priyadarshana and Sofronov (2012a), Priyadarshana and Sofronov (2012b)).
	"""
	
	homepage = "https://github.com/madawaweer/breakpoint"
	cran = "breakpoint" 

	version("1.2", md5="29f7a10de45145ded1029f9fd25c9883")

	depends_on("r@2.5:", type=("build", "run"))
	depends_on("r-ggplot2@1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-msm@1.0.1:", type=("build", "run"))
	depends_on("r-foreach@1.2:", type=("build", "run"))
	depends_on("r-doparallel@1.0.10:", type=("build", "run"))
