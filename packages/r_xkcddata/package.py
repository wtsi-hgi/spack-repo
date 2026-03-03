# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXkcddata(RPackage):
	"""Get XKCD Comic Data

	Download data from individual XKCD comics, written by Randall Munroe <https://xkcd.com/>.
	"""
	
	cran = "XKCDdata" 

	version("0.1.0", md5="6226a1293f206b5a91c27af9f2e3c183")

	depends_on("r-httr@1.3.1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-tibble@1.3.4:", type=("build", "run"))
	depends_on("r-dplyr@0.7.4:", type=("build", "run"))
	depends_on("r-jsonlite@1.5:", type=("build", "run"))
	depends_on("r-glue@1.1.1:", type=("build", "run"))
	depends_on("r-htmltools@0.3.6:", type=("build", "run"))
	depends_on("r-assertthat@0.2:", type=("build", "run"))
