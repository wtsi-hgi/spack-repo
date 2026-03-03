# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCim(RPackage):
	"""Compositional Impact of Migration

	Produces statistical indicators of the impact of migration on the socio-demographic
	composition of an area. Three measures can be used: ratios, percentages and the Duncan index
	of dissimilarity. The input data files are assumed to be in an  origin-destination matrix format,
	with each cell representing a flow count between an origin and a destination area. Columns are expected
	to represent origins, and rows are expected to represent destinations. The first row and column are
	assumed to contain labels for each area. See Rodriguez-Vignoli and Rowe (2018)
	<doi:10.1080/00324728.2017.1416155> for technical details.
	"""
	
	cran = "CIM" 

	version("1.0.0", md5="cd26ef648707733d23527e22db6f41f8")

	depends_on("r@3.4:", type=("build", "run"))
