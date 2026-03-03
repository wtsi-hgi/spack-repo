# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdar(RPackage):
	"""Individual Diversity-Area Relationships

	Computes and tests individual (species, phylogenetic and functional) diversity-area relationships, i.e., how species-, phylogenetic- and functional-diversity varies with spatial scale around the individuals of some species in a community. See applications of these methods in Wiegand et al. (2007) <doi:10.1073/pnas.0705621104> or Chacon-Labella et al. (2016) <doi:10.1007/s00442-016-3547-z>.
	"""
	
	cran = "idar" 

	version("1.5", md5="0d47ad7e215e6a5b53fae14291c0bf75")

	depends_on("r-fd", type=("build", "run"))
	depends_on("r-picante", type=("build", "run"))
	depends_on("r-spatstat@2.0.0:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-spatstat-random", type=("build", "run"))
