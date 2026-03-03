# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMappp(RPackage):
	"""Map in Parallel with Progress

	Provides one function, which is a wrapper around purrr::map() with some extras on top, including parallel computation, progress bars, error handling, and result caching.
	"""
	
	homepage = "https://github.com/cole-brokamp/mappp"
	cran = "mappp" 

	version("1.0.0", md5="fe4c973fabedc1ad9fa9cf9047a7510f")

	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-pbmcapply", type=("build", "run"))
	depends_on("r-parallelly", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
