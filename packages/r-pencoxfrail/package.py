# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPencoxfrail(RPackage):
	"""Regularization in Cox Frailty Models

	A regularization approach for Cox Frailty Models by penalization methods is provided.
	"""
	
	cran = "PenCoxFrail" 

	version("1.0.1", md5="492bc1dc832018f0cc2ecd72929a8c56")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
