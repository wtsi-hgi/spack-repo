# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCalpassapi(RPackage):
	"""R Interface to Access CalPASS API

	Implements methods for querying data from CalPASS using its API.
 CalPASS Plus.  MMAP API V1. <https://mmap.calpassplus.org/docs/index.html>.
	"""
	
	homepage = "https://github.com/vinhdizzo/calpassapi"
	cran = "calpassapi" 

	version("0.0.3", md5="3a1a6d5d8f4d4840134da16b9311ecb9")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
