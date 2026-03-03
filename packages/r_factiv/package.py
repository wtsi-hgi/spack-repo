# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFactiv(RPackage):
	"""Instrumental Variables Estimation for 2^k Factorial Experiments

	Implements instrumental variable estimators for 2^K factorial experiments with noncompliance.
	"""
	
	homepage = "https://github.com/mattblackwell/factiv"
	cran = "factiv" 

	version("0.1.0", md5="f7f5fa513574dc1e94b92b6056621831")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
