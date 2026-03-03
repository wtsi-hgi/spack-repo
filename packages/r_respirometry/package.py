# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRespirometry(RPackage):
	"""Tools for Conducting and Analyzing Respirometry Experiments

	Provides tools to enable the researcher to more precisely conduct
    respirometry experiments. Strong emphasis is on aquatic respirometry. Tools
    focus on helping the researcher setup and conduct experiments. Functions for
    analysis of resulting respirometry data are also provided. This package
    provides tools for intermittent, flow-through, and closed respirometry
    techniques.
	"""
	
	cran = "respirometry" 

	version("1.5.0", md5="f7501a9413700302d470b0ba8132327d")

	depends_on("r-birk", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-marelac", type=("build", "run"))
	depends_on("r-measurements@1.1:", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-seacarb@3.1:", type=("build", "run"))
	depends_on("r-segmented@1.0.0:", type=("build", "run"))
