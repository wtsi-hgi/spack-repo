# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGtfs2gps(RPackage):
	"""Converting Transport Data from GTFS Format to GPS-Like Records

	Convert general transit feed specification (GTFS) data to global positioning system (GPS) records in 'data.table' format. It also has some functions to subset GTFS data in time and space and to convert both representations to simple feature format.
	"""
	
	homepage = "https://github.com/ipeaGIT/gtfs2gps"
	cran = "gtfs2gps" 

	version("2.1-1", md5="bf449898e6eb405e17b0191a2f495469")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-gtfstools", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-sfheaders", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-lwgeom", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
