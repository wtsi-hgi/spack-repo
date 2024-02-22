# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlrpro(RPackage):
	"""Stepwise Regression with Assumptions Checking

	The stepwise regression with assumptions checking and the possible Box-Cox transformation.
	"""
	
	cran = "mlrpro" 

	version("0.1.2", md5="900ed84dfda3c7d49f13647f533bae17")

	depends_on("r-car", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
