# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsotoper(RPackage):
	"""Stable Isotope Mixing Model

	Estimates diet contributions from isotopic sources using JAGS.
    Includes estimation of concentration dependence and measurement error.
	"""
	
	cran = "IsotopeR" 

	version("0.5.4", md5="268d5fa6f8b00f0bbe3b5b38512f937c")

	depends_on("r-fgui", type=("build", "run"))
	depends_on("r-runjags", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
