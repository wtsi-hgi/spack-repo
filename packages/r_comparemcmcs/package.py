# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComparemcmcs(RPackage):
	"""Compare MCMC Efficiency from 'nimble' and/or Other MCMC Engines

	Manages comparison of MCMC performance metrics from multiple MCMC algorithms. These may come from different MCMC configurations using the 'nimble' package or from other packages. Plug-ins for JAGS via 'rjags' and Stan via 'rstan' are provided. It is possible to write plug-ins for other packages. Performance metrics are held in an MCMCresult class along with samples and timing data. It is easy to apply new performance metrics. Reports are generated as html pages with figures comparing sets of runs. It is possible to configure the html pages, including providing new figure components.
	"""
	
	homepage = "https://github.com/nimble-dev/compareMCMCs"
	cran = "compareMCMCs" 

	version("0.5.0", md5="28f6c3edec1f71f65300f036f7d56bec")

	depends_on("r-nimble", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
