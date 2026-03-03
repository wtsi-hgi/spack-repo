# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMdw(RPackage):
	"""Maximum Diversity Weighting

	Dimension-reduction methods aim at defining a score that maximizes signal diversity. Three approaches, tree weight, maximum entropy weights, and maximum variance weights are provided. These methods are described in He and Fong (2019) <DOI:10.1002/sim.8212>.
	"""
	
	cran = "mdw" 

	version("2020.6-17", md5="c77441221c9bff1391bf24270a68075c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-kyotil", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
