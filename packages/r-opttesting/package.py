# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpttesting(RPackage):
	"""Optimal Testing

	Optimal testing under general dependence. The R package implements procedures proposed in Wang, Han, and Tong (2022). The package includes parameter estimation procedures, the computation for the posterior probabilities, and the testing procedure.
	"""
	
	cran = "OPTtesting" 

	version("1.0.0", md5="8d602a38a218b2913acc575dd7a3b5e9")

	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
