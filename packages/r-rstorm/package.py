# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRstorm(RPackage):
	"""Simulate and Develop Streaming Processing

	While streaming processing provides opportunities to deal with extremely large and ever growing data sets in (near) real time, the development of streaming algorithms for complex models is often cumbersome: the software packages that facilitate streaming processing in production environments do not provide statisticians with the simulation, estimation, and plotting tools they are used to. Developers of streaming algorithms would thus benefit from the flexibility of [R] to create, plot and compute data while developing streaming algorithms. Package RStorm implements a streaming architecture modeled on Storm for easy development and testing of streaming algorithms in [R]. RStorm is not intended as a production package, but rather a development tool for streaming algorithms. 
	"""
	
	cran = "RStorm" 

	version("1.0", md5="e00a5d0997d5c93ba82a50eb74546751")

	depends_on("r-plyr", type=("build", "run"))
