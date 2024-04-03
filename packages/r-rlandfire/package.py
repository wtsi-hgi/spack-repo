# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRlandfire(RPackage):
	"""Interface to 'LANDFIRE Product Service' API

	Provides access to a suite of geospatial data layers for wildfire management, fuel modeling, ecology, natural resource management, climate, conservation, etc., via the 'LANDFIRE' (<https://www.landfire.gov/index.php>) Product Service ('LFPS') API.
	"""
	
	homepage = "https://github.com/bcknr/rlandfire"
	cran = "rlandfire" 

	version("1.0.0", md5="abc424fe54ab57209ccf3492093f27a0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
