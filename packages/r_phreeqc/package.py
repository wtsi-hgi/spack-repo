# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhreeqc(RPackage):
	"""R Interface to Geochemical Modeling Software

	A geochemical modeling program developed by the US Geological
    Survey that is designed to perform a wide variety of aqueous geochemical
    calculations, including speciation, batch-reaction, one-dimensional 
    reactive-transport, and inverse geochemical calculations.
	"""
	
	homepage = "https://www.usgs.gov/software/phreeqc-version-3"
	cran = "phreeqc" 

	version("3.7.6", md5="f99d5584cf9e7de22b6372939ff93c02")

	depends_on("r@3.5:", type=("build", "run"))
