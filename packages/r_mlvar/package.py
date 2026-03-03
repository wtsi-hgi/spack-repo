# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlvar(RPackage):
	"""Multi-Level Vector Autoregression

	Estimates the multi-level vector autoregression model on time-series data.
             Three network structures are obtained: temporal networks, contemporaneous
             networks and between-subjects networks.
	"""
	
	cran = "mlVAR" 

	version("0.5.2", md5="6c7777865e4e07d16ed4571f434c3ba8")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-arm", type=("build", "run"))
	depends_on("r-qgraph", type=("build", "run"))
	depends_on("r-dplyr@0.5:", type=("build", "run"))
	depends_on("r-clustergeneration", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-mplusautomation", type=("build", "run"))
	depends_on("r-graphicalvar", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
