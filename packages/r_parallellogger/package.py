# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParallellogger(RPackage):
	"""Support for Parallel Computation, Logging, and Function
Automation

	Support for parallel computation with progress bar, and option to stop or proceed on errors. Also provides logging to console and disk,
  and the logging persists in the parallel threads. Additional functions support function call automation with delayed execution (e.g. for executing functions in
  parallel).
	"""
	
	homepage = "https://ohdsi.github.io/ParallelLogger/"
	cran = "ParallelLogger" 

	version("3.3.0", md5="edc695abdcdf9408438ffb78823b075c")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-snow", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
