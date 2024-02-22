# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetworkriskmeasures(RPackage):
	"""Risk Measures for (Financial) Networks

	Implements some risk measures for (financial) networks, such as DebtRank, Impact Susceptibility, Impact Diffusion and Impact Fluidity. 
	"""
	
	homepage = "https://github.com/carloscinelli/NetworkRiskMeasures"
	cran = "NetworkRiskMeasures" 

	version("0.1.4", md5="d9e12f7a952f3b62f09b50f15286bb8b")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
