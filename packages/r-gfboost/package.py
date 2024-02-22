# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGfboost(RPackage):
	"""Gradient-Free Gradient Boosting

	Implementation of routines of the author's PhD thesis on gradient-free Gradient Boosting (Werner, Tino (2020) "Gradient-Free Gradient Boosting", URL '<https://oops.uni-oldenburg.de/id/eprint/4290>').
	"""
	
	cran = "gfboost" 

	version("0.1.1", md5="df0f44d440a9af94d11f43a95d572626")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-pcapp", type=("build", "run"))
	depends_on("r-mboost", type=("build", "run"))
