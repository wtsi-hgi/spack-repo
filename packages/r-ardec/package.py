# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArdec(RPackage):
	"""Time Series Autoregressive-Based Decomposition

	Autoregressive-based decomposition of a time series based on the approach in West (1997). Particular cases include the extraction of trend and seasonal components.
	"""
	
	cran = "ArDec" 

	version("2.1-1", md5="b39975b0fd574184c1dd76c4b67ba711")

