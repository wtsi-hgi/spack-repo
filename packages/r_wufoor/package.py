# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWufoor(RPackage):
	"""R Wrapper for the 'Wufoo.com' - The Form Building Service

	Allows form managers to download entries from their respondents
    using Wufoo JSON API (<https://www.wufoo.com>). Additionally, the Wufoo reports - when public - can be
    also acquired programmatically. Note that building new forms within this package
    is not supported.
	"""
	
	homepage = "https://github.com/dmpe/wufoor"
	cran = "WufooR" 

	version("1.0.1", md5="ae9547340ba891cdfe058687cb766650")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-httr@1.4.1:", type=("build", "run"))
	depends_on("r-jsonlite@1.6.1:", type=("build", "run"))
	depends_on("r-dplyr@0.8.5:", type=("build", "run"))
