# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCccm(RPackage):
	"""Crossed Classification Credibility Model

	Calculates the credit debt for the next period based on the available data using the cross-classification credibility model.
	"""
	
	cran = "cccm" 

	version("0.1.0", md5="684ad21b225bd465666e39a74a6501e4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
