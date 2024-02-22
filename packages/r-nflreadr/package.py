# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNflreadr(RPackage):
	"""Download 'nflverse' Data

	A minimal package for downloading data from 'GitHub'
    repositories of the 'nflverse' project.
	"""
	
	homepage = "https://nflreadr.nflverse.com"
	cran = "nflreadr" 

	version("1.4.0", md5="2fbf96e9d1d4e7e7c4a8ecccb2a5361c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cachem@1:", type=("build", "run"))
	depends_on("r-cli@3:", type=("build", "run"))
	depends_on("r-curl@4.3:", type=("build", "run"))
	depends_on("r-data-table@1.14:", type=("build", "run"))
	depends_on("r-glue@1.4:", type=("build", "run"))
	depends_on("r-memoise@2:", type=("build", "run"))
	depends_on("r-rappdirs@0.3:", type=("build", "run"))
	depends_on("r-rlang@0.4.10:", type=("build", "run"))
