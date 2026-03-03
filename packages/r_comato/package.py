# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComato(RPackage):
	"""Analysis of Concept Maps and Concept Landscapes

	Provides methods for the import/export and automated analysis of concept maps and concept landscapes (sets of concept maps).
	"""
	
	cran = "comato" 

	version("1.1", md5="985136c02345adc5ca354fd4fa099b63")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-gdata", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-clustersim", type=("build", "run"))
