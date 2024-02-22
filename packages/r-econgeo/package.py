# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcongeo(RPackage):
	"""Computing Key Indicators of the Spatial Distribution of Economic
Activities

	Computes a series of indices commonly used in the fields of economic geography, economic complexity, and evolutionary economics to describe the location, distribution, spatial organization, structure, and complexity of economic activities. Functions include basic spatial indicators such as the location quotient, the Krugman specialization index, the Herfindahl or the Shannon entropy indices but also more advanced functions to compute different forms of normalized relatedness between economic activities or network-based measures of economic complexity. Most of the functions use matrix calculus and are based on bipartite (incidence) matrices consisting of region - industry pairs. These are described in Balland (2017) <http://econ.geo.uu.nl/peeg/peeg1709.pdf>.
	"""
	
	homepage = "https://github.com/PABalland/EconGeo"
	cran = "EconGeo" 

	version("2.0", md5="c6c73607b5ba480dc5c02294204da975")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
