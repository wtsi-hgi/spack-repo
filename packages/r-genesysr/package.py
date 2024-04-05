# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenesysr(RPackage):
	"""Genesys PGR Client

	Access data on plant genetic resources from genebanks around the world published on Genesys (<https://www.genesys-pgr.org>).
  Your use of data is subject to terms and conditions available at <https://www.genesys-pgr.org/content/legal/terms>.
	"""
	
	homepage = "https://gitlab.croptrust.org/genesys-pgr/genesysr"
	cran = "genesysr" 

	version("2.1.1", md5="b602b9f2d509c92f412242538b304d5e")
	version("2.1.0", md5="136b481c2d0ac75d5dbea8d1a378d82e")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-httr2@1:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
