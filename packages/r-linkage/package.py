# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLinkage(RPackage):
	"""Clustering Communication Networks Using the Stochastic Topic
Block Model Through Linkage.fr

	It allows to cluster communication networks using the Stochastic
  Topic Block Model <doi:10.1007/s11222-016-9713-7> by posting jobs through 
  the API of the linkage.fr server, which implements the clustering method.
  The package also allows to visualize the clustering results returned by the server.
	"""
	
	cran = "Linkage" 

	version("0.9", md5="28907ed47730abeb1852a83f8f303249")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
