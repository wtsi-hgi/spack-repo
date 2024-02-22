# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDalsm(RPackage):
	"""Nonparametric Double Additive Location-Scale Model (DALSM)

	Fit of a double additive location-scale model with a nonparametric error distribution from possibly right- or interval censored data. The additive terms in the location and dispersion submodels, as well as the unknown error distribution in the location-scale model, are estimated using Laplace P-splines. For more details, see Lambert (2021) <doi:10.1016/j.csda.2021.107250>.
	"""
	
	homepage = "<https://github.com/plambertULiege/DALSM>"
	cran = "DALSM" 

	version("0.9.1", md5="884a3153b6b6a294961569c2237e7cd5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cubicbsplines", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
