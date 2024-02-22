# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRchoice(RPackage):
	"""Discrete Choice (Binary, Poisson and Ordered) Models with Random
Parameters

	An implementation of simulated maximum likelihood method for the estimation of Binary (Probit and Logit), Ordered (Probit and Logit) and Poisson models with random parameters for cross-sectional and longitudinal data as presented in Sarrias (2016) <doi:10.18637/jss.v074.i10>.
	"""
	
	homepage = "https://github.com/mauricio1986/Rchoice"
	cran = "Rchoice" 

	version("0.3-6", md5="63567a18d22ae152e5537c25eff8dc21")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-maxlik", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-misctools", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-memisc", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-plm", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
