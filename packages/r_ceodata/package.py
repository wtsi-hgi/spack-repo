# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCeodata(RPackage):
	"""Datasets of the CEO (Centre d'Estudis d'Opinio) for Opinion
Polls in Catalonia

	Easy and convenient access to the datasets of the
  "Centre d'Estudis d'Opinio", the Catalan institution for polling and public
  opinion. The package uses the data stored in the servers of the CEO and returns
  it in a tidy format.
	"""
	
	homepage = "https://ceo.gencat.cat/ca/inici/"
	cran = "CEOdata" 

	version("1.3.1.1", md5="1a610107ee292e61b9464e9005b06414")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
