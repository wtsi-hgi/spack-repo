# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrefine(RPackage):
	"""r Client for OpenRefine API

	'OpenRefine' (formerly 'Google Refine') is a popular, open source data cleaning software. This package enables users to programmatically trigger data transfer between R and 'OpenRefine'. Available functionality includes project import, export and deletion.
	"""
	
	homepage = "https://github.com/vpnagraj/rrefine"
	cran = "rrefine" 

	version("2.1.0", md5="362e0bc9960edb692aaf51c3edb13f9e")

	depends_on("r-httr@1.1:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
