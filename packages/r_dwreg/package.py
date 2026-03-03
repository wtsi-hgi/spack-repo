# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDwreg(RPackage):
	"""Parametric Regression for Discrete Response

	Regression for a discrete response, where the conditional distribution is modelled via a discrete Weibull distribution.
	"""
	
	cran = "DWreg" 

	version("2.0", md5="41286e21081aae4cd2c1e841d4a63396")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-maxlik", type=("build", "run"))
	depends_on("r-discreteweibull", type=("build", "run"))
	depends_on("r-ecdat", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
