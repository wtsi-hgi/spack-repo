# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpiralize(RPackage):
	"""Visualize Data on Spirals

	It visualizes data along an Archimedean spiral <https://en.wikipedia.org/wiki/Archimedean_spiral>, makes so-called spiral graph or spiral chart. 
    It has two major advantages for visualization: 1. It is able to visualize data with very long axis with high 
    resolution. 2. It is efficient for time series data to reveal periodic patterns.
	"""
	
	homepage = "https://github.com/jokergoo/spiralize"
	cran = "spiralize" 

	version("1.0.6", md5="3a898626e8b0eb2c780952db674f2b7c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-globaloptions@0.1.1:", type=("build", "run"))
	depends_on("r-getoptlong@0.1.8:", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
