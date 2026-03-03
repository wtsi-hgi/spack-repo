# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUniah(RPackage):
	"""Unimodal Additive Hazards Model

	Nonparametric estimation of a unimodal or U-shape covariate effect under additive hazards model.
	"""
	
	cran = "uniah" 

	version("1.2", md5="9f7fa5df82b3a70a5b442f55fd33045c")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-iso", type=("build", "run"))
	depends_on("r-ahaz", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
