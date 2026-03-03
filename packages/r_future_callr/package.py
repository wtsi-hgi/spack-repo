# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFutureCallr(RPackage):
	"""A Future API for Parallel Processing using 'callr'

	Implementation of the Future API on top of the 'callr' package.  This allows you to process futures, as defined by the 'future' package, in parallel out of the box, on your local (Linux, macOS, Windows, ...) machine.  Contrary to backends relying on the 'parallel' package (e.g. 'future::multisession') and socket connections, the 'callr' backend provided here can run more than 125 parallel R processes.
	"""
	
	homepage = "https://future.callr.futureverse.org"
	cran = "future.callr" 

	version("0.8.2", md5="4291f1fc951e92a4f960a527205bdca4")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-future@1.33:", type=("build", "run"))
	depends_on("r-callr@2.0.3:", type=("build", "run"))
