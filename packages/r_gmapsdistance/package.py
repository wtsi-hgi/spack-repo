# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmapsdistance(RPackage):
	"""Distance and Travel Time Between Two Points from Google Maps

	Get distance and travel time between two points from Google Maps.
    Four possible modes of transportation (bicycling, walking, driving and
    public transportation).
	"""
	
	homepage = "https://github.com/jlacko/gmapsdistance"
	cran = "gmapsdistance" 

	version("4.0.4", md5="d48e344e29947128f48eb78c3a6df830")

	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
