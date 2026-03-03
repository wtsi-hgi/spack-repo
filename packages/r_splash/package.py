# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSplash(RPackage):
	"""Simple Process-Led Algorithms for Simulating Habitats

	This program calculates bioclimatic indices and fluxes (radiation, 
    evapotranspiration, soil moisture) for use in studies of ecosystem function, 
    species distribution, and vegetation dynamics under changing climate 
    scenarios. Predictions are based on a minimum of required inputs: latitude, 
    precipitation, air temperature, and cloudiness. 
    Davis et al. (2017) <doi:10.5194/gmd-10-689-2017>.
	"""
	
	homepage = "https://github.com/villegar/splash/"
	cran = "splash" 

	version("1.0.2", md5="af1fc0994d457b0ef17d083985797263")

	depends_on("r@3.2.3:", type=("build", "run"))
