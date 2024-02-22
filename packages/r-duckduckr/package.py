# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDuckduckr(RPackage):
	"""Simple Client for the DuckDuckGo Instant Answer API

	Programmatic access to the DuckDuckGo Instant Answer API <https://api.duckduckgo.com/api>.
	"""
	
	homepage = "https://github.com/dirkschumacher/duckduckr"
	cran = "duckduckr" 

	version("1.0.0", md5="b32a7742089c7ee1d6a095bc26afdd7a")

	depends_on("r-crul", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
