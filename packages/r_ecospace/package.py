# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcospace(RPackage):
	"""Simulating Community Assembly and Ecological Diversification
Using Ecospace Frameworks

	Implements stochastic simulations of community assembly (ecological
    diversification) using customizable ecospace frameworks (functional trait
    spaces). Provides a wrapper to calculate common ecological disparity and
    functional ecology statistical dynamics as a function of species richness.
    Functions are written so they will work in a parallel-computing environment.
	"""
	
	homepage = "https://github.com/pnovack-gottshall/ecospace"
	cran = "ecospace" 

	version("1.4.2", md5="22c589920b81b4b2f3c46a0db7f66f21")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-fd@1.0.12:", type=("build", "run"))
