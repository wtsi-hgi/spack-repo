# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPh1xbar(RPackage):
	"""Phase I Shewhart X-Bar Chart

	The purpose of 'PH1XBAR' is to build a Phase I Shewhart control chart for the basic Shewhart, the variance components and the ARMA models in R for subgrouped and individual data. More details can be found: Yao and Chakraborti (2020) <doi: 10.1002/qre.2793>, and Yao and Chakraborti (2021) <doi: 10.1080/08982112.2021.1878220>.
	"""
	
	homepage = "https://github.com/bolus123/PH1XBAR"
	cran = "PH1XBAR" 

	version("0.11.1", md5="4aa7da9c1da254d9c92104678bcfc231")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
