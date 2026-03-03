# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRaquifer(RPackage):
	"""Estimate the Water Influx into Hydrocarbon Reservoirs

	Generate a table of cumulative water influx into hydrocarbon reservoirs over time using un-steady and pseudo-steady state models. Van Everdingen, A. F. and Hurst, W. (1949) <doi:10.2118/949305-G>. Fetkovich, M. J. (1971) <doi:10.2118/2603-PA>. Yildiz, T. and Khosravi, A. (2007) <doi:10.2118/103283-PA>. 
	"""
	
	homepage = "https://susaenergy.github.io/Raquifer_ws/"
	cran = "Raquifer" 

	version("0.1.0", md5="ffbee397b4f9af2103b8171c891a80d0")

	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
