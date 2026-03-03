# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcondemand(RPackage):
	"""General Analysis of Various Economics Demand Systems

	Tools for general properties including price, quantity, elasticity, convexity, marginal revenue and manifold of various economics demand systems including Linear, Translog, CES, LES and CREMR.
	"""
	
	cran = "EconDemand" 

	version("1.0", md5="6c2fff756852b2d2a1f95534ff8c7cfa")

	depends_on("r@3.2.2:", type=("build", "run"))
