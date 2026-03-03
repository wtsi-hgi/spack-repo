# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcsurv(RPackage):
	"""Semiparametric Regression Analysis of Interval-Censored Data

	Currently using the proportional hazards (PH) model. More methods under other semiparametric regression models will be included in later versions. 
	"""
	
	cran = "ICsurv" 

	version("1.0.1", md5="86b97089e556ffcfed62b91e4db664be")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass@7.3.33:", type=("build", "run"))
	depends_on("r-matrixcalc@1.0.3:", type=("build", "run"))
