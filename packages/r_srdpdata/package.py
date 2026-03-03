# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSrdpdata(RPackage):
	"""Strategies of Resistance Data Project

	Provides you with easy, programmatic access to SRDP data.
	"""
	
	homepage = "https://github.com/hgoers/sRdpData"
	cran = "sRdpData" 

	version("0.1.0", md5="ebde9d945c3a0e6527535ae419ddac1f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
