# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpectator(RPackage):
	"""Interface to the 'Spectator Earth' API

	Provides interface to the 'Spectator Earth' API <https://api.spectator.earth/>, 
    mainly for obtaining the acquisition plans and satellite overpasses for Sentinel-1, 
    Sentinel-2, Landsat-8 and Landsat-9 satellites. Current position and trajectory can 
    also be obtained for a much larger set of satellites. It is also possible to search 
    the archive for available images over the area of interest for a given (past) period, 
    get the URL links to download the whole image tiles, or alternatively to download the 
    image for just the area of interest based on selected spectral bands.
	"""
	
	cran = "spectator" 

	version("0.2.0", md5="187137900442377382a2f516d0a229f3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-geojsonsf", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
