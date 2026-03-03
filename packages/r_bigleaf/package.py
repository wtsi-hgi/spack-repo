# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBigleaf(RPackage):
	"""Physical and Physiological Ecosystem Properties from Eddy
Covariance Data

	Calculation of physical (e.g. aerodynamic conductance, surface temperature), 
             and physiological (e.g. canopy conductance, water-use efficiency) ecosystem properties
			 from eddy covariance data and accompanying meteorological measurements. Calculations
			 assume the land surface to behave like a 'big-leaf' and return bulk ecosystem/canopy variables.
	"""
	
	homepage = "https://bitbucket.org/juergenknauer/bigleaf"
	cran = "bigleaf" 

	version("0.8.2", md5="5e7e0d3976a6678e5ba42007bb2dc13c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-solartime", type=("build", "run"))
