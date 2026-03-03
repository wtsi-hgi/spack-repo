# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlightsbr(RPackage):
	"""Download Flight and Airport Data from Brazil

	Download flight and airport data from Brazil’s Civil Aviation Agency
             (ANAC) <https://www.gov.br/anac>. The data includes detailed 
             information on all aircrafts, aerodromes, airports, and airport 
             movements registered in ANAC, on airfares and on every international
             flight to and from Brazil, as well as domestic flights within the country.
	"""
	
	homepage = "https://github.com/ipeaGIT/flightsbr"
	cran = "flightsbr" 

	version("0.4.0", md5="e7f5580ec5a0ffa681fec33e9b935fbd")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table@1.14:", type=("build", "run"))
	depends_on("r-httr@1.4.1:", type=("build", "run"))
	depends_on("r-parzer", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
