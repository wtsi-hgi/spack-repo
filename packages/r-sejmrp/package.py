# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSejmrp(RPackage):
	"""An Information About Deputies and Votings in Polish Diet from
Seventh to Eighth Term of Office

	Set of functions that access information about deputies and votings
    in Polish diet from webpage <http://www.sejm.gov.pl>. The package was developed
    as a result of an internship in MI2 Group - <http://mi2.mini.pw.edu.pl>, Faculty
    of Mathematics and Information Science, Warsaw University of Technology.
	"""
	
	cran = "sejmRP" 

	version("1.3.4", md5="1663ddea2fec234f15c74b031944cba3")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-factoextra", type=("build", "run"))
	depends_on("r-rpostgresql", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
