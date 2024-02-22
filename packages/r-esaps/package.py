# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REsaps(RPackage):
	"""Indicators of Electoral Systems and Party Systems

	It allows structuring electoral data of different size and structure 
        to calculate various indicators frequently used in the studies of electoral systems and party systems.
        Indicators of electoral volatility, electoral disproportionality, party nationalization and the 
        effective number of parties are included.
	"""
	
	homepage = "https://github.com/Nicolas-Schmidt/esaps"
	cran = "esaps" 

	version("0.2.2", md5="e1093e05db1b780e804aea1945891813")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
	depends_on("r-readods@1.6.4:", type=("build", "run"))
	depends_on("r-readxl@1:", type=("build", "run"))
