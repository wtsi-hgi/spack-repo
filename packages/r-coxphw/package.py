# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoxphw(RPackage):
	"""Weighted Estimation in Cox Regression

	Implements weighted estimation in Cox regression as proposed by
             Schemper, Wakounig and Heinze (Statistics in Medicine, 2009, 
             <doi:10.1002/sim.3623>) and as described in Dunkler, Ploner, Schemper and 
             Heinze (Journal of Statistical Software, 2018, <doi:10.18637/jss.v084.i02>). 
             Weighted Cox regression provides unbiased average hazard ratio 
             estimates also in case of non-proportional hazards. 
             Approximated generalized concordance probability an effect size measure for clear-cut
             decisions can be obtained.
             The package provides options to estimate time-dependent effects conveniently by
             including interactions of covariates with arbitrary functions of time, with or without
             making use of the weighting option.
	"""
	
	homepage = "https://github.com/biometrician/coxphw"
	cran = "coxphw" 

	version("4.0.3", md5="1aee001f567e7bcd568ee3c4e6fa1fe6")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
