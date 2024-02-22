# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarelac(RPackage):
	"""Tools for Aquatic Sciences

	Datasets, constants, conversion factors, and utilities for 'MArine', 'Riverine',
             'Estuarine', 'LAcustrine' and 'Coastal' science. 
             The package contains among others: (1) chemical and
             physical constants and datasets, e.g. atomic weights, gas
             constants, the earths bathymetry; (2) conversion factors
             (e.g. gram to mol to liter, barometric units,
             temperature, salinity); (3) physical functions, e.g. to
             estimate concentrations of conservative substances, gas
             transfer and diffusion coefficients, the Coriolis force
             and gravity; (4) thermophysical properties of the
             seawater, as from the UNESCO polynomial or from the more
             recent derivation based on a Gibbs function.
	"""
	
	cran = "marelac" 

	version("2.1.11", md5="1a19e7e63ea61cfe124f6485485df0b5")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-shape", type=("build", "run"))
	depends_on("r-seacarb", type=("build", "run"))
