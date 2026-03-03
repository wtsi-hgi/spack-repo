# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpportunistic(RPackage):
	"""Routing Distribution, Broadcasts, Transmissions and Receptions
in an Opportunistic Network

	Computes the routing distribution, the expectation of the number of broadcasts, transmissions and receptions considering an Opportunistic transport model. It provides theoretical results and also estimated values based on Monte Carlo simulations.
	"""
	
	cran = "Opportunistic" 

	version("1.2", md5="d38163408aa4e868a3adfb50b9994917")

