# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKoboconnectr(RPackage):
	"""Download Data from Kobotoolbox to R

	Wrapper for 'Kobotoolbox' APIs ver 2 mentioned at <https://support.kobotoolbox.org/api.html>, to download data from 'Kobotoolbox' to R. Small and simple package that adds immense convenience for the data professionals using 'Kobotoolbox'.
	"""
	
	homepage = "https://github.com/asitav-sen/KoboconnectR"
	cran = "KoboconnectR" 

	version("1.2.2", md5="cce6e1cf1601bc1b1f76e1aa966f5540")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-mime", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
