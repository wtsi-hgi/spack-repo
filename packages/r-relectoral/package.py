# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRelectoral(RPackage):
	"""Electoral Analysis

	Functions to obtain an important number of electoral indicators described in the package, which can be divided into two large sections: The first would be the one containing the indicators of electoral disproportionality, such as, Rae index, Loosemore–Hanby index, etc. The second group is intended to study the dimensions of the party system vote, through the indicators of electoral fragmentation, polarization, volatility, etc. Moreover, multiple seat allocation simulations can also be performed based on different allocation systems, such as the D'Hondt method, Sainte-Laguë, etc. Finally, some of these functions have been built so that, if the user wishes, the data provided by the Spanish Ministry of Home Office for different electoral processes held in Spain can be obtained automatically. All the above will allow the users to carry out deep studies on the results obtained in any type of electoral process. The methods are described in: Oñate, Pablo and Ocaña, Francisco A. (1999, ISBN:9788474762815); Ruiz Rodríguez, Leticia M. and Otero Felipe, Patricia (2011, ISBN:9788474766226).
	"""
	
	cran = "Relectoral" 

	version("0.1.0", md5="1bea76a0f81e8870fb1c2d98df551035")

	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-xlsx", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
