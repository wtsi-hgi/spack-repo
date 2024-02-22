# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRformatter(RPackage):
	"""R Source Code Formatter

	The R Formatter formats R source code. It is very much based on
    formatR, but tries to improve it by heuristics. For example, spaces can be
    forced around the division operator "/".
	"""
	
	homepage = "https://github.com/evolutics/RFormatter"
	cran = "RFormatter" 

	version("0.1.1", md5="48e18bf80b02f0bb1f510a168b6f5824")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-formatr@1.2.1:", type=("build", "run"))
