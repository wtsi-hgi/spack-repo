# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLinerr(RPackage):
	"""Linear Excess Relative Risk Model

	Fits a linear excess relative risk model by maximum likelihood, possibly including several variables and allowing for lagged exposures.
	"""
	
	cran = "linERR" 

	version("1.0", md5="681ef4e5eef0c3dbe30823b3a51b5db8")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
