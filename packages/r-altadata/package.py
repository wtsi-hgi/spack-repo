# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAltadata(RPackage):
	"""API Wrapper for Altadata.io

	Functions for interacting directly with the 'ALTADATA' API. With this R package, developers can build applications around the 'ALTADATA' API without having to deal with accessing and managing requests and responses. 'ALTADATA' is a curated data marketplace for more information go to <https://www.altadata.io>.
	"""
	
	homepage = "https://github.com/altabering/altadata-r"
	cran = "altadata" 

	version("0.1.1", md5="d802b6b5bd387c72146d5d9d9daf713b")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-httr@0.6.1:", type=("build", "run"))
	depends_on("r-jsonlite@0.9.14:", type=("build", "run"))
