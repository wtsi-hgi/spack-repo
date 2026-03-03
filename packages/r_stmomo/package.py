# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStmomo(RPackage):
	"""Stochastic Mortality Modelling

	Implementation of the family of generalised age-period-cohort
    stochastic mortality models. This family of models encompasses many models
    proposed in the actuarial and demographic literature including the 
    Lee-Carter (1992) <doi:10.2307/2290201> and
    the Cairns-Blake-Dowd (2006) <doi:10.1111/j.1539-6975.2006.00195.x> models. 
    It includes functions for fitting mortality models, analysing their 
    goodness-of-fit and performing mortality projections and simulations.
	"""
	
	homepage = "http://github.com/amvillegas/StMoMo"
	cran = "StMoMo" 

	version("0.4.1", md5="a71eb7c815ef7e74c53d344820360281")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-gnm@1:", type=("build", "run"))
	depends_on("r-forecast@6.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rootsolve@1.6.5.1:", type=("build", "run"))
	depends_on("r-fanplot@3.4:", type=("build", "run"))
	depends_on("r-reshape2@1.4.1:", type=("build", "run"))
	depends_on("r-fields@8.2:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
