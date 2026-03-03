# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDompi(RPackage):
	"""Foreach Parallel Adaptor for the Rmpi Package

	Provides a parallel backend for the %dopar% function using
        the Rmpi package.
	"""
	
	cran = "doMPI" 

	version("0.2.2", md5="d183e73f909a8d125992b0d37bc7beb6")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-foreach@1.3:", type=("build", "run"))
	depends_on("r-iterators@1:", type=("build", "run"))
	depends_on("r-rmpi@0.5.7:", type=("build", "run"))
