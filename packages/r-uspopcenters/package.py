# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUspopcenters(RPackage):
	"""United States Centers of Population (Centroids)

	Centers of population (centroid) data for census areas in the
    United States.
	"""
	
	homepage = "https://www.census.gov/geographies/reference-files/time-series/geo/centers-population.html"
	cran = "USpopcenters" 

	version("0.2.0", md5="32c4ecb7a5fd415ff6640f730bbfc8c2")

	depends_on("r@2.10:", type=("build", "run"))
