# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmmpar(RPackage):
	"""Parallel Linear Mixed Model

	Embarrassingly Parallel Linear Mixed Model calculations spread across local cores which repeat until convergence.
	"""
	
	homepage = "https://github.com/fulyagokalp/lmmpar"
	cran = "lmmpar" 

	version("0.1.0", md5="039c82abfacd7938da46196545ef6a5c")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-bigmemory", type=("build", "run"))
