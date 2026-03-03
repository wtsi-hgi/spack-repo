# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHarbinger(RPackage):
	"""A Unified Time Series Event Detection Framework

	By analyzing time series, it is possible to observe significant changes in the behavior of observations that frequently characterize events. Events present themselves as anomalies, change points, or motifs. In the literature, there are several methods for detecting events. However, searching for a suitable time series method is a complex task, especially considering that the nature of events is often unknown. This work presents Harbinger, a framework for integrating and analyzing event detection methods. Harbinger contains several state-of-the-art methods described in Salles et al. (2020) <doi:10.5753/sbbd.2020.13626>.
	"""
	
	homepage = "https://github.com/cefet-rj-dal/harbinger"
	cran = "harbinger" 

	version("1.0.767", md5="e0f424e01d24b5c42dbfb75e6fa6ad2f")
	version("1.0.737", md5="216b0b74c597f7e2491239d9c88faa9e")

	depends_on("r-daltoolbox", type=("build", "run"))
	depends_on("r-tsmp", type=("build", "run"))
	depends_on("r-dtwclust", type=("build", "run"))
	depends_on("r-rugarch", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-changepoint", type=("build", "run"))
	depends_on("r-strucchange", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-wavelets", type=("build", "run"))
	depends_on("r-hht", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
