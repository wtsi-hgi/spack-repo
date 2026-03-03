# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmplik(RPackage):
	"""Empirical Likelihood Ratio for Censored/Truncated Data

	Empirical likelihood ratio tests for means/quantiles/hazards
 	from possibly censored and/or truncated data. Now does regression too.
	This version contains some C code.
	"""
	
	homepage = "http://www.ms.uky.edu/~mai/EmpLik.html"
	cran = "emplik" 

	version("1.3-1", md5="ebc34ff86a25d4a20f113e0b0f004720")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
