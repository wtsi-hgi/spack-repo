# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBss(RPackage):
	"""Brownian Semistationary Processes

	Efficient simulation of Brownian semistationary (BSS) processes using the hybrid simulation scheme, as described in 
    Bennedsen, Lunde, Pakkannen (2017) <arXiv:1507.03004v4>, as well as functions to fit BSS processes
    to data, and functions to estimate the stochastic volatility process of a BSS process.
	"""
	
	cran = "BSS" 

	version("0.1.0", md5="95069ea53ee38673e817ae2d87d3efe5")

	depends_on("r-hypergeo", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-phangorn", type=("build", "run"))
