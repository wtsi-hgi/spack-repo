# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REctsvr(RPackage):
	"""Cointegration Based Support Vector Regression Model

	The cointegration based support vector regression model enables researchers to use data obtained from the cointegrating vector as input in the support vector regression model.
	"""
	
	cran = "ECTSVR" 

	version("0.1.0", md5="162b3443a1cbc8778e116f340f593abb")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-urca", type=("build", "run"))
	depends_on("r-vars", type=("build", "run"))
	depends_on("r-weightsvm", type=("build", "run"))
