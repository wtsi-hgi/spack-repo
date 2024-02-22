# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLgarch(RPackage):
	"""Simulation and Estimation of Log-GARCH Models

	Simulation and estimation of univariate and multivariate log-GARCH models. The main functions of the package are: lgarchSim(), mlgarchSim(), lgarch() and mlgarch(). The first two functions simulate from a univariate and a multivariate log-GARCH model, respectively, whereas the latter two estimate a univariate and multivariate log-GARCH model, respectively.
	"""
	
	homepage = "http://www.sucarrat.net/"
	cran = "lgarch" 

	version("0.6-2", md5="b6702c15ceb72deeb4b600f35a625798")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
