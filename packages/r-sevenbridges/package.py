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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/sevenbridges_1.32.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/sevenbridges/sevenbridges_1.32.0.tar.gz"]

	version("1.32.0", md5="1c204add9c56d7518a5362b99111ec18")

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
