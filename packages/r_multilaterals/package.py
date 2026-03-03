# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultilaterals(RPackage):
	"""Transitive Index Numbers for Cross-Sections and Panel Data

	Computing transitive (and non-transitive) index numbers (Coelli et al., 2005 <doi:10.1007/b136381>) for cross-sections and panel data. For the calculation of transitive indexes, the EKS (Coelli et al., 2005 <doi:10.1007/b136381>; Rao et al., 2002 <doi:10.1007/978-1-4615-0851-9_4>) and Minimum spanning tree (Hill, 2004 <doi:10.1257/0002828043052178>) methods are implemented. Traditional fixed-base and chained indexes, and their growth rates, can also be derived using the Paasche, Laspeyres, Fisher and Tornqvist formulas. 
	"""
	
	cran = "multilaterals" 

	version("1.0", md5="64b4137539996ff5a185c54b01a8846a")

	depends_on("r-ape", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
