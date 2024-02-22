# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDhis2r(RPackage):
	"""Client for the 'DHIS2' Web API

	Connect and pull data from a 'DHIS2 (District Health Information Software 2)' instance into R.
	"""
	
	homepage = "https://github.com/amanyiraho/dhis2r"
	cran = "dhis2r" 

	version("0.1.1", md5="6cc1acc829e6e524358898c735dff0b0")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-attempt@0.3.1:", type=("build", "run"))
	depends_on("r-curl@4.3.3:", type=("build", "run"))
	depends_on("r-dplyr@1.0.10:", type=("build", "run"))
	depends_on("r-httr2@0.2.2:", type=("build", "run"))
	depends_on("r-r6@2.5.1:", type=("build", "run"))
