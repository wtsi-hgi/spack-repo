# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHowzatr(RPackage):
	"""Useful Functions for Cricket Analysis

	Helping to calculate cricket specific problems in a tidy & simple manner.
	"""
	
	homepage = "https://github.com/lukelockley/howzatR"
	cran = "howzatR" 

	version("1.0.1", md5="8e5118c17fe754fcf5461a010c586944")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
