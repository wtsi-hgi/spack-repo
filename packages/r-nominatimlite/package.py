# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNominatimlite(RPackage):
	"""Interface with 'Nominatim' API Service

	Lite interface for getting data from 'OSM' service
    'Nominatim' <https://nominatim.org/release-docs/latest/>. Extract
    coordinates from addresses, find places near a set of coordinates and
    return spatial objects on 'sf' format.
	"""
	
	homepage = "https://dieghernan.github.io/nominatimlite/"
	cran = "nominatimlite" 

	version("0.3.0", md5="56f9b3214cf7a0e6978232489de320b1")
	version("0.2.1", md5="61e45302686d71a6583a3954b6a38ab7")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-jsonlite@1.7:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-sf@0.9:", type=("build", "run"))
