# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSevenbridges(RPackage):
	"""Seven Bridges Platform API Client and Common Workflow Language Tool Builder in R

	R client and utilities for Seven Bridges platform API, from Cancer Genomics Cloud to other Seven Bridges supported platforms.
	"""
	
	homepage = "https://www.sevenbridges.com"
	bioc = "sevenbridges"

	version("1.38.0", commit="7e22d1c7757c770b98a93691a8cd7f161c5ee4a3")
	version("1.32.0", commit="bd309cce2719e2074733ca5926e496439cb61faa")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-objectproperties", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-docopt", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
