# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROsrm(RPackage):
	"""Interface Between R and the OpenStreetMap-Based Routing Service
OSRM

	An interface between R and the 'OSRM' API. 'OSRM' is a routing
    service based on 'OpenStreetMap' data. See <http://project-osrm.org/> for more
    information. This package enables the computation of routes, trips, isochrones and
    travel distances matrices (travel time and kilometric distance).
	"""
	
	homepage = "https://github.com/riatelab/osrm"
	cran = "osrm" 

	version("4.1.1", md5="f955c12d2eb81d8db4b1bd24481283e5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcppsimdjson", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-mapiso", type=("build", "run"))
	depends_on("r-googlepolylines", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
