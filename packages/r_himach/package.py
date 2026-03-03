# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHimach(RPackage):
	"""High Mach Finds Routes for Supersonic Aircraft

	For supersonic aircraft, flying subsonic over land,
    find the best route between airports. Allow for coastal buffer and
    potentially closed regions. Use a minimal model of aircraft
    performance: the focus is on time saved versus subsonic flight, rather
    than on vertical flight profile. For modelling and forecasting, not for planning your
    flight!
	"""
	
	homepage = "https://github.com/david6marsh/himach"
	cran = "himach" 

	version("0.3.2", md5="3c711f169c9bd24289802ed2c3f60b59")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cpprouting", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lwgeom", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-s2", type=("build", "run"))
	depends_on("r-sf@1:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
