# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJrich(RPackage):
	"""Jack-Knife Support for Evolutionary Distinctiveness Indices I
and W

	These functions calculate the taxonomic measures presented in Miranda-Esquivel (2016). 
   The package introduces Jack-knife resampling in evolutionary distinctiveness prioritization analysis, 
   as a way to evaluate the support of the ranking in area prioritization, and the persistence of a given area 
   in a conservation analysis.
   The algorithm is described in: Miranda-Esquivel, D (2016) <DOI:10.1007/978-3-319-22461-9_11>.
	"""
	
	homepage = "https://github.com/Dmirandae/jrich"
	cran = "jrich" 

	version("0.60-35", md5="c3de43009033afab7c1d41720b70f6df")

	depends_on("r-ape", type=("build", "run"))
